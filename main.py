from fastapi import FastAPI
from fastapi import FastAPI
from utils.router_loader import load_routers
import routers

app = FastAPI()

load_routers(app, routers)
@app.get("/")
async def root():
    return {"message": "What are you seeking for?"}