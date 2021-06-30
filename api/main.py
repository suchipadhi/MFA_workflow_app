from fastapi import FastAPI
from api.utils.dbutils import database
from api.auth import route as auth_router
from api.opts_emails import router as opt_router
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="FastAPI (Python)",
    description="FastAPI Framework",
    version="1.0",
    openapi_url="/openapi.json"
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(auth_router.router, tags=["Auth"])
app.include_router(opt_router.router, tags=["OTPs"])