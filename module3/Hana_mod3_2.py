from fastapi import FastAPI
from datetime import datetime

app=FastAPI()
@app.get("/message")
def message(text:str):
    return{
        "message":text,
        "timestamp":datetime.utcnow().isoformat()
    }








