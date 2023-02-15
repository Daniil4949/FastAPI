import uvicorn
from app.models import User as ModelUser
from app.schema import User as SchemaUser, UserOut, TokenSchema, SystemUser
from app.app_conf import app
from app.utils import verify_password, get_hashed_password, \
    create_access_token, create_refresh_token
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.deps import get_current_user


@app.post("/sign_up/")
async def create_user(user: SchemaUser):
    user_id = await ModelUser.create(**user.dict())
    return {"user_id": user_id}


@app.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user


@app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await ModelUser.get_by_name(form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )

    return {
        "access_token": create_access_token(user['id']),
        "refresh_token": create_refresh_token(user['id']),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
