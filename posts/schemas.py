from fastapi import FastAPI, HTTPException, Request
from typing import Dict, Optional
from pydantic import BaseModel

# CRUD
# Create Read Update Delete
# post    get      put        delete
#username
#name
#surname
#age
#gender




class CreateUserRequest (BaseModel):
    username: Optional [str]
    name: Optional [str]
    surname: Optional [str]
    age: Optional [int]
    gender: Optional [str]

class EditUserRequest (BaseModel):
    username: Optional [str] = None
    name: Optional [str] = None
    surname: Optional [str] = None
    age: Optional [int] = None
    gender: Optional [str] = None






