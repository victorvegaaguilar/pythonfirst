from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM="HS256"
ACCESS_TOKEN_DURATION=1
# openssl rand -hex 32
SECRET="88a48f31e98f0fef49a2f380717eea7a28e2fd7288897ed8ee96d4423cc0de66"

router = APIRouter(prefix="/jwt", 
                   tags=["jwt_auth"],
                   responses={404: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


# Entidad user

class User(BaseModel):
    username:str
    full_name:str
    email:str
    disabled:bool

class UserDB(User):
    password:str

users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "$2a$12$bpz5itZtg0nhq.Xd805lGO3311oNNeMn771/lYBvxFNrHTpSKJY7u"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "password": "$2a$12$AqaTCWI3aIQUbndJakjmeuAn12fM7VmVLishicN9Iu4JWEvErx112"
    }

}

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no existe2")

    user = search_user_db(form.username)
    if user is None:
        raise HTTPException(status_code=400, detail="El usuario no existe2")

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="La clave no es correcta")

    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire = datetime.utcnow() + access_token_expiration

    access_token = {"sub":user.username, "exp":expire}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM, ), "token_type":"bearer"}

async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user