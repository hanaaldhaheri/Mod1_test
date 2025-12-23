from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
app=FastAPI()

@app.post("/api/text")
async def handle_text(request:Request):
    bdy = await request.body()
    print('got request', bdy)
    try:
        data = await request.json()
        print('data', data)
        if "Text" not in data:
            return JSONResponse(
                status_code=442,
                content={
                    "error": "Text field is required"
                }
            )
        return{
            "message": "Success",
                "Text": data["Text"]
            }
    except json.JSONDecodeError as msg:
        print(msg)
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid JSON body"}
        )