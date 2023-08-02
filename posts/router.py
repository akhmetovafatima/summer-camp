from fastapi import FastAPI, HTTPException, Request, APIRouter
from typing import Dict, Optional
from pydantic import BaseModel
from posts.schemas import CreateUserRequest, EditUserRequest

router = APIRouter()



users = {}


last_added_user_id = -1

@router.get('/users')
def get_users():
    return users

@router.post('/users')
def create_user(user: CreateUserRequest):
    global last_added_user_id
    new_id = last_added_user_id + 1
    users[new_id] = user
    last_added_user_id = new_id
    return new_id

@router.get('/user/{id}')
def get_user(id: int):
    if id not in users: 
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

    return users[id]

    return id

@router.put('/user/{id}')
def edit_user(id: int, user: EditUserRequest):
    if id not in users: 
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

    for key, value in users.dict().items():
        if value is not None:
            users[id][key] = value

    return id

@router.delete('/user/{id}')
def edit_user(id: int):
    if id not in users: 
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

    del users[id]

    return id

