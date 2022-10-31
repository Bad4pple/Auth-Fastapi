from fastapi import APIRouter , Depends
from typing import List
from app import schemas 
from app.auth import jwt_bearer

router = APIRouter()

db = [
    {
        'id': 1,
        'title': 'untitled ggez',
        'content': 'dsafjkskadfjaskfjkals jksdfjasdkfj klsdjf ksdjfsdj fskdfjk 😸'
    }
]

@router.get("/")
async def get_posts() -> List[dict]:
    return db

@router.get("/{id}")
async def get_id(id: int):
    if id < len(db) or id > len(db):
        return {'message': f'id: {id} not found'}
        
    for index in  db:
        if index["id"] == id:
            return index
    return {'message': f'id: {id} not found'}

@router.post('/',dependencies=[Depends(jwt_bearer.JWTBearer())])
async def create_post(request: schemas.PostSchema):
    db.append(request.dict())
    return request.dict()

