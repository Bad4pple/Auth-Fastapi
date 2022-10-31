from fastapi import APIRouter
from app.routers import auth , post

router = APIRouter()

router.include_router(router=auth.router, prefix='/auth', tags=['Auth'])
router.include_router(router=post.router, prefix='/post', tags=['Post'])