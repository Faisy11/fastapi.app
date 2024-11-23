from crud.user_crud import create_user as create_user_crud
from fastapi import APIRouter
from typing import Dict
from models.user_model import User_model

router = APIRouter()

@router.post('/create_user', response_model=Dict[str, str])
def create_user_route(user:User_model):
    if user.username and user.password:
        result = create_user_crud(user.username, user.password)
        if result:
            return result
        else:
            return {"message": "Failed to create user"}
    else:
        return {"message": "Username and password are required"}
