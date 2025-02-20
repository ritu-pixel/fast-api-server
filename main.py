from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "Ritu Rajput",  "Location": "Dehradun"}

@app.get("/{data}")
def read_root(data: str):
    return {"Hey, There!": data, "Location": "Dehradun"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
