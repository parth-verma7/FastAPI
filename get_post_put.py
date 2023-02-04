from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: str
    
class UpdateItem(BaseModel):
    name:Optional[str]=None,
    price:Optional[float]=None,
    brand:Optional[str]=None
    
inventory={
    
}

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
    # inventory[item_id]={"name":item.name,"price":item.price,"brand":item.brand}
    inventory[item_id]=item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item:UpdateItem,item_id:int):
    if item_id not in inventory:
        return {"message":"Item not found"}
    if item.name!=None:
        inventory[item_id].name=item.name
    if item.brand!=None:
        inventory[item_id].brand=item.brand
    if item.price!=None:
        inventory[item_id].price=item.price
    return inventory[item_id]