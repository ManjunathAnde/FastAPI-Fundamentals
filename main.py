from fastapi import FastAPI
from models import Products
from database import db_session,engine
import database_models

database_models.dec_base.metadata.create_all(bind=engine)
#create a table with all metadata in dec_base class and bind it with engine (db_url constant connection)

app = FastAPI() #creating an instance of FASTAPI

@app.get("/") # using GET HTTP method to see information in homepage
def greet():
    return "Welcome to MJ APP"

products = [  #Instantiating the classes
    Products(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Products(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Products(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Products(id=4, name="Table", description="A wooden table", price=199.99, quantity=20)
]

def init_db():
    db = db_session() #creating a session of linking with db
    existing = db.query(database_models.Products).first()
    if not existing: #checks if atleast one row exists in db, adds if no informaiton exists
        for product in products:
            db.add(database_models.Products(**product.model_dump()))
        db.commit()
    db.close()

@app.get("/products") #using GET method to display information when the user routes to 'products' in the web app. 
def get_products():
    # db=db_session()
    # db.query
    return products

sno:int=1
@app.get("/products/{sno}") #A dynamic URL to fetch products by ID
def get_single_product(sno:int): 
    for product in products: #Looking up the product roster to find matching ID
        if product.id == sno:
            return{'message': 'Hurray! Product found',
                   'prod_details': product
                   } #If found, return the instance.
    return {"error": f"Product with ID {sno} not found"} #error handling

@app.post("/products")
def add_product(input:Products): #accepting input in form of Products and appending to roster
    products.append(input)
    return {"message":"Add successful", "item" : input}

print(products)

@app.put("/products")
def update_product(id:int,product:Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product update successful"
    return "Product not found"

@app.delete("/products")
def delete_product (id:int,product:Products):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deletion successful"
    return "Product not found"