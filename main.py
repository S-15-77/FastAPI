from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/file")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)