from sqlalchemy.orm import sessionmaker #single interaction/transaction as user hits the endpoint
from sqlalchemy import create_engine #permanent main pipeline between python and db until FASTAPI server is running.

db_url = "mysql+pymysql://root:12345@127.0.0.1:3306/fastapi_db" #points to schema in db in MySQL
engine = create_engine(db_url)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#bind connects the session to the specific DB
#autoflush=false: holds the data in RAM until complete request is formed. Then sents it to db
#autocommit=false: provides the manual commit button to the database to ensure record consistency.
