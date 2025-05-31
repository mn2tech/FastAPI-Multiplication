from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/multiply")
async def multiply(data: Numbers):
    return {"result": data.num1 * data.num2}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains; you can specify allowed origins instead of "*"
    allow_methods=["*"],
    allow_headers=["*"],
)