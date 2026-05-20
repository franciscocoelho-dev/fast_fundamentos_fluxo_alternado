from fastapi import FastAPI
# as (alias) se comporta como um apelido do elemento importando
from sistema_estudos.routers.produtos import router as router_produtos

# Objeto de FastAPI, permitindo o consumo de todos os recursos da biblioteca (framework)
app = FastAPI()

# Como as rotas estão dentro do diretório routers, é necessário fazer a inclusão de todas as rotas no objeto app.
app.include_router(router=router_produtos, prefix='/api/produto', tags=['produto'])

