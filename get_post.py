from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand:Optional[str]=None

    
inventory={}

@app.get("/get-by-name")
def namechange(name:str=None):
    for key in inventory:
        # if key.name == name:
        return inventory[key]
    return {"Data":"Not Found"}
    
@app.post("/create-item/{item_id}")
def create_item(item:Item,item_id:int):
    if item_id in inventory:
        return {"message":"Item already exists"}
    inventory[item_id]=item
    return inventory[item_id]

