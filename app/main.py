from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get("/leads")
def leads():
    return {"leads":"all leads here"}