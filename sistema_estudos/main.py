from fastapi import FastAPI
from sistema_estudos.routers.produtos import router as router_user

app = FastAPI()
app.include_router(
    router=router_user,
    prefix='/api/produto',
    tags=['produtos']
)

