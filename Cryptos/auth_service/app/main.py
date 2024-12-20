from fastapi import FastAPI

from Cryptos.auth_service.app.routes.v1.user import router

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)