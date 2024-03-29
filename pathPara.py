from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id", item_id}
async def read_item(item_id : int):
    return {"item_id", item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)