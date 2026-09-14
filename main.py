from fastapi import FastAPI, Depends
from models import Products
from database import db_session, engine
import database_models
from sqlalchemy.orm import Session

database_models.dec_base.metadata.create_all(bind=engine)
#create a table with all metadata in dec_base class and bind it with engine (db_url constant connection)

app = FastAPI() #creating an instance of FASTAPI

@app.get("/") # using GET HTTP method to see information in homepage
def greet():
    return "Welcome to MJ APP"

#Dependency Injection
def get_db():
    try: ##Establish the connection and hand the active session to the function
        db_session_open = db_session()
        yield db_session_open
    finally: #Close the active session at the end of function, regardless of status of execution.
        db_session_open.close()

@app.get("/products") #using GET method to display information when the user routes to 'products' in the web app.
def get_products(db: Session = Depends(get_db)): #get_products depends on session connection with db
    return db.query(database_models.Products).all()

@app.get("/products/{id}") #A dynamic URL to fetch products by ID
def get_single_product(id: int, db: Session = Depends(get_db)):
    product_with_id = db.query(database_models.Products).filter(database_models.Products.id == id).first() #filter to match product id. If multiple, return first one
    if product_with_id:
        return {'message': 'Hurray! Product found',
                'prod_details': product_with_id} #If found, return the product object.
    return {"error": f"Product with ID {id} not found"} #error handling

@app.post("/products")
def add_product(input: Products, db: Session = Depends(get_db)): #accepting input in form of Products and saving to db
    new_product = database_models.Products(
        name=input.name,
        description=input.description,
        price=input.price,
        quantity=input.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product) #refresh to get the auto-generated id from db
    return {"message": "Add successful", "item": new_product}

@app.put("/products/{id}")
def update_product(id: int, product: Products, db: Session = Depends(get_db)):
    existing = db.query(database_models.Products).filter(database_models.Products.id == id).first()
    if not existing:
        return {"error": "Product not found"}
    existing.name = product.name
    existing.description = product.description
    existing.price = product.price
    existing.quantity = product.quantity
    db.commit()
    return {"message": "Product update successful"}

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)): #only needs id, no request body required
    existing = db.query(database_models.Products).filter(database_models.Products.id == id).first()
    if not existing:
        return {"error": "Product not found"}
    db.delete(existing)
    db.commit()
    return {"message": "Product deletion successful"}