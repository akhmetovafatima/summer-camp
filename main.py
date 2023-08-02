from fastapi import FastAPI
from typing import Dict, Optional
from pydantic import BaseModel
#from posts.router import router

# CRUD
# Create Read Update Delete
# post    get      put        delete



app = FastAPI()

app.include_router(router, prefix="/posts")




users = {}

last_added_user = -1

class CreateUserRequest (BaseModel):
    username: Optional [str]
    name: Optional [str]
    surname: Optional [str]
    age: Optional [int]
    gender: Optional [str]

class UpdateUserRequest (BaseModel):
    username: Optional [str] = None
    name: Optional [str] = None
    surname: Optional [str] = None
    age: Optional [int] = None
    gender: Optional [str] = None

 
@app.get('/users')
def get_users():
    return users


@app.post('/users')
def create_user(user: CreateUserRequest):
   global last_added_user_id
   new_id = last_added_user_id + 1
   users[new_id] = user
last_added_user_id = new_id


return new_id


@app.get('/user/{id}')
def get_user(id: int):
   if id not in users: 
      raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

   return users[id]

   return id

 @app.put('/user/{id}')
 def edit_user(id: int, user: UpdateUserRequest):
   if id not in users: 
      raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

 for key, value in user.dict().items():
       if value is not None:
           users[id][key] = value

  return id

 @app.delete('/user/{id}')
def edit_user(id: int):
   if id not in users: 
        raise HTTPException(status_code=404, detail=f'No user with id {id} was found')

   del users[id]

    return id

#def dict (
       # include: IncEx = None,
        #exclude
#)
#Dict[str, Any]
















