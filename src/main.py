from src.model import User
from typing import Optional
from fastapi import FastAPI, HTTPException, Header


app = FastAPI()


@app.get("/auth/authorization/")
async def auth_authorization(Authorization: Optional[str] = Header(None)):
    if Authorization == 'admin':
        raise HTTPException(
            status_code=200,
            headers={"X-User-ID": Authorization}
        )
    else:
        raise HTTPException(
            status_code=403,
            headers={"X-User-ID": Authorization}
        )


@app.post("/auth/password/")
async def auth_password(user: User):
    if user.name == 'admin' and user.password == 'admin':
        raise HTTPException(
            status_code=200,
            headers={"X-User-ID": user.name}
        )
    else:
        raise HTTPException(
            status_code=403,
            detail="user not found"
        )
