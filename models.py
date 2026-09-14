from pydantic import BaseModel
from typing import Optional #Basemodel is the tool FASTAPI uses to give a blueprint API expects

class Products (BaseModel): 
    id: Optional[int]=None #Using Python Hints to predefine data types
    name:str
    description:str
    price:float
    quantity:int
#Pydantic takes care of the constructor
