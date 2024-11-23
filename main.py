from fastapi import FastAPI
from router import user_router
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
app = FastAPI()
from typing import Union

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(user_router.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application"}
