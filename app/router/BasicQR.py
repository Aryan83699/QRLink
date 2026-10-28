import qrcode 
from fastapi import APIRouter,Request
from fastapi.responses import JSONResponse


router=APIRouter()


@router.post("/api/base-qr")
async def generate_base_qr(request:Request):
    data=await request.json()

    if not data:
        return JSONResponse(content={"Error":"Invalid Data"},status_code=422)

    