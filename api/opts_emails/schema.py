from pydantic import BaseModel, Field


class CreateOTP(BaseModel):
    recipent_id: str


class Verify_OTP(CreateOTP):
    session_id: str
    opt_code: str


class OTPList(Verify_OTP):
    session_id: str
    opt_code: str
