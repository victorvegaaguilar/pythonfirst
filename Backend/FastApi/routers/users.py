#from fastapi import FastAPI, HTTPException
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import starlette

#app = FastAPI()
router = APIRouter()

# Entidad user

class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int

    
users_list = [User(id= 1, name = "Victor", surname="Vega", age=35),
            User(id= 2, name = "Alex", surname="Sanchez", age=45),
            User(id= 3, name = "Roberto", surname="Torres", age=55),]



@router.get("/usersjson")
async def usersjson():
    return [{"name": "Victor", "surname": "Victor", "age": 10},
            {"name": "Alex", "surname": "Sanchez", "age": 20},
            {"name": "Roberto", "surname": "Torres", "age": 30},]

@router.get("/usersclass")
async def usersclass():
    return User(id= 1, name = "Victor", surname="Vega", age=35)

@router.get("/users")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id: int):
    users  = filter(lambda user: user.id == id, users_list )
    try:
        return list(users)
    except:
        raise HTTPException(404, detail="Se produjo un error.")

@router.get("/userquery/")
async def userquery(id: int):
    return search_user(id)


@router.post("/user/", response_model=User, status_code=201)
async def user_add(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(404, detail="No se ha encontrado usuario")
    else:
        users_list.append(user)
        return search_user(user.id)


@router.put("/user/")
async def user_update(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha encontrado usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user_delete(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha encontrado usuario"}

    return users_list


def search_user(id: int):
    users  = filter(lambda user: user.id == id, users_list )
    try:
        return list(users)
    except:
        return {"error": "No se ha encontrado usuario"}


