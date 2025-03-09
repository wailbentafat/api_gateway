from fastapi import FastAPI , Request# type: ignore
from fastapi_api_gateway.app.rate_limiter import init_rate_limiter
import uvicorn # type: ignore
from app.routes import app
from app.logger import logger

@app.on_event("startup")
async def startup():
    await init_rate_limiter()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    
    logger.info(f"Request: {request.method} {request.url}")
    
    response = await call_next(request)
    
    logger.info(f"Response: {response.status_code}")
    return response

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
