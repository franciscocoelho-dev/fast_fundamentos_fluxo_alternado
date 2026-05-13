from fastapi import FastAPI
from sistema_estudos.routers.produtos import router as router_produtos

app = FastAPI()
app.include_router(
    router=router_produtos,
    prefix='/api/produto',
    tags=['produto']
)

