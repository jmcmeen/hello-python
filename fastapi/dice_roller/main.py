# run "uvicorn main:app --reload" from the terminal
from fastapi import FastAPI
from dice import roll_dice

app = FastAPI()

@app.get("/")
async def roll_6():
    return {"sides": 6,
            "roll": roll_dice(6)}


@app.get("/{sides}")
async def roll_sides(sides: int):
    return {"sides": sides,
            "roll": roll_dice(sides)}
