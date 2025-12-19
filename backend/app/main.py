from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import Base, engine
from app.routes.auth_routes import router as auth_router
from app.routes.auth_otp_routes import router as auth_otp_router
from app.routes.admin_auth_routes import router as admin_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://192.168.175.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(auth_otp_router)