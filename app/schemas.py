from pydantic import BaseModel , Field , EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)  

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "How to drink a water",
                "content": "1. drink water 2. successfully how to drink water"
            }
        }

class UserSchema(BaseModel):
    email: EmailStr = Field(default = None)
    password: str = Field(default = None)

    class Config:
        schema_extra = {
            "user_demo": {
                "email": "iamroot@root.com",
                "password": "!IAMRoot$cat&sl"
            }
        }

class UserCreate(UserSchema):
    pass