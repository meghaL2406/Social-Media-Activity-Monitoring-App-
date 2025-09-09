from fastapi import *
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Pydantic model for incoming login requests
class LoginRequest(BaseModel):
    channel_link : str


@app.post('/tel-login')
async def tel_login(request: LoginRequest):

    channel_link = request.channel_link
    print(channel_link)
    
    return {"message": "Login successful"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=5100)