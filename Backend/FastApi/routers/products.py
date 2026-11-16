#from fastapi import FastAPI, HTTPException
from fastapi import APIRouter, HTTPException

product_list = ["Producto11", "Producto2", "Producto3", "Producto4", "Producto5"]

#app = FastAPI()
#router = APIRouter()
router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message": "No encontrado"}})

@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id:int):
    return product_list[id]