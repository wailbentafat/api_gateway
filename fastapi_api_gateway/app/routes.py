from fastapi import FastAPI, Depends, Request, HTTPException
from app.auth import create_access_token, verify_token
from datetime import timedelta
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES, MICROSERVICES
from pydantic import BaseModel
import httpx
from fastapi_limiter.depends import RateLimiter
from app.logger import logger
app = FastAPI()
class TokenRequest(BaseModel):
    username: str
    role: str


@app.get("/health")
def health_check():
    return {"status": "API Gateway is running"}

@app.post("/token")
def generate_token(request: TokenRequest):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": request.username, "role": request.role}, access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(current_user: dict = Depends(verify_token)):
    return {"message": "Access granted", "user": current_user}
@app.get("/proxy/{service}/{path:path}",dependencies=[Depends(RateLimiter(times=5, minutes=1))])
async def proxy_request(service: str, path: str, request: Request, current_user: dict = Depends(verify_token)):
    if service not in MICROSERVICES:
        raise HTTPException(status_code=404, detail="Service not found")
    
    url = f"{MICROSERVICES[service]}/{path}"
    
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            url,
            params=request.query_params,
            headers={"Authorization": f"Bearer {request.headers.get('Authorization', '')}"}
        )
    
    if response.status_code >= 400:
        logger.error(f"Error proxying request to {url}: {response.status_code}")
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()
