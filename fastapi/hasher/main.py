# run "uvicorn main:app --reload" from the terminal
from fastapi import FastAPI
from hash import md5hash

app = FastAPI()

@app.get("/md5/{input_text}")
async def roll_sides(input_text: str):
    return {"input": input_text,
            "output": md5hash(input_text)}
