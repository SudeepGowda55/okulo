from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    username: str
    password: str

@app.get("/")
async def root():
    return "homepage"

@app.post("/login")
async def login(data: Login):
    print(data)
    return "login credentials received"