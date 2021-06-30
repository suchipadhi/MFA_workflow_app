from fastapi import APIRouter, HTTPException
from api.opts_emails import schema
from api.enums import opt


router = APIRouter(prefix="/api/v1")


@router.post("/otp/send")
async def send_opt():
    return "Sending OTP"


@router.post("/otp/verify")
async def verify_opt():
    return "Verifying OTP"
