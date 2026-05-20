from fastapi import APIRouter, status
from sistema_estudos.schemas.produtos import ProdutoListPublicSchema, ProdutoPublicSchema, ProdutoSchema, ProdutoUpdateSchema
from typing import Optional, List
from sistema_estudos.db import PRODUTOS

router = APIRouter()

# -------------------------------------------
# Criar as rotas(endpoints) de Produto
# -------------------------------------------

@router.get(path='/', response_model=ProdutoListPublicSchema, status_code=status.HTTP_200_OK)
def produto_list():
    return {'produtos': PRODUTOS}


@router.post(path='/', response_model=ProdutoPublicSchema, status_code=status.HTTP_201_CREATED)
def produto_create(produto: ProdutoSchema):
    produto_id = ProdutoPublicSchema(**produto.model_dump(), id=len(PRODUTOS)+1)
    PRODUTOS.append(produto_id)
    return produto_id

@router.put(path='/{id: int}', response_model=ProdutoPublicSchema, status_code=status.HTTP_201_CREATED)
def produto_update(id_produto: int, produto: ProdutoUpdateSchema):
    produto_editado = ProdutoPublicSchema(**produto.model_dump(), id=id_produto)
    PRODUTOS[id_produto - 1] = produto_editado
    return produto_editado

@router.delete(path='/{id: int}')
def produto_delete(id_produto: int):
    del PRODUTOS[id_produto - 1]
    return 

