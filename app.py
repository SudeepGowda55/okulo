from fastapi import APIRouter
from pydantic import BaseModel

app_router = APIRouter()

class Register(BaseModel):
    username: str
    password: str

@app_router.post("/register")
async def register(data: Register):
    print(data)
    return "registration successful"