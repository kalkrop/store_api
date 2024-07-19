from fastapi import APIRouter

from store.controllers import product


api_router = APIRouter()
api_router.include_router(product, prefix="/products")
