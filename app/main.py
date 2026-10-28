from fastapi import FastAPI,APIRouter
import uvicorn
from db.database import create_tables,get_db,engine
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    await engine.dispose()



app=FastAPI(title="QRLink" , summary="Authentication less QR code generator and URL shortener using FARM    Stack ",version="1.0",redoc_url=False,docs_url=False,lifespan=lifespan)


app.add_middleware(CORSMiddleware,
                   allow_credentials=["*"],
                   allow_headers=["*"],
                   allow_methods=["*"],
                   allow_origins=["*"])


@app.get("/")
def root():
    return {"message":"hello"}








