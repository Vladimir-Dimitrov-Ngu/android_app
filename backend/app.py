import uvicorn
from backend.api import router as router_fastapi
from fastapi import FastAPI

app_fastapi = FastAPI()
app_fastapi.include_router(router_fastapi)


if __name__ == "__main__":
    uvicorn.run(app_fastapi, host="0.0.0.0", port=9002)
