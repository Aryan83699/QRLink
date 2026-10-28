from fastapi import FastAPI
import uvicorn
from db.database import create_tables,get_db,engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await engine.dispose()



app=FastAPI(title="QRLink" , summary="Authentication less QR code generator and URL shortener using FARM    Stack ",version="1.0",redoc_url=False,docs_url=False,lifespan=lifespan)



@app.get("/")
def root():
    return {"message":"hello"}






