from fastapi import APIRouter , Body
from app.auth.jwt_handler import signJWT
from app import schemas

fake_db = [
    
]

def check_user(data: schemas.UserSchema):
    for user in fake_db:
        if user["email"] == data.email and user['password'] == data.password:
            return True
        return False


router = APIRouter()

@router.post("/register")
async def register(request: schemas.UserCreate = Body(default = None)):
    fake_db.append(request.dict())
    return signJWT(request.email)

@router.post("/login")
async def login(request: schemas.UserSchema = Body(default = None)):
    if check_user(request):
        return signJWT(request.email)
    else:
        return {"Error": "Invalid username or password"}