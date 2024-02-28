from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item.name.upper()
    return item

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)