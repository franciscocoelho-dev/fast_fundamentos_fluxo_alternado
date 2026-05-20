from fastapi import APIRouter, status, HTTPException
from sistema_estudos.schemas.produtos import ProdutoListPublicSchema, ProdutoPublicSchema, ProdutoSchema, ProdutoUpdateSchema
from typing import Optional, List
from sistema_estudos.db import PRODUTOS

router = APIRouter()

# -------------------------------------------
# Criar as rotas(endpoints) de Produto
# -------------------------------------------

@router.get(path='/', response_model=ProdutoListPublicSchema, status_code=status.HTTP_200_OK)
def produto_list():
    # Retorna a lista com todos os produtos cadastrados
    return {'produtos': PRODUTOS}


@router.post(path='/', response_model=ProdutoPublicSchema, status_code=status.HTTP_201_CREATED)
def produto_create(produto: ProdutoSchema):
    # A função model_dump() desestrutura o objeto para ser compreendido como um json
    produto_id = ProdutoPublicSchema(**produto.model_dump(), id=len(PRODUTOS)+1)
    PRODUTOS.append(produto_id)
    return produto_id


@router.put(path='/{id: int}', response_model=ProdutoPublicSchema, status_code=status.HTTP_201_CREATED)
def produto_update(id_produto: int, produto: ProdutoUpdateSchema):
    # Verifica se o id_produto está maior no intervalo de 1 ao tamanho da lista, caso contrário dispara (raise) uma exception de "Usuário não encontrado".
    if id_produto > len(PRODUTOS) or id_produto < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found')
    
    produto_editado = ProdutoPublicSchema(**produto.model_dump(), id=id_produto)
    PRODUTOS[id_produto - 1] = produto_editado
    return produto_editado


@router.delete(path='/{id: int}')
def produto_delete(id_produto: int):
    # Mesma validação realizada no produto_update
    if id_produto > len(PRODUTOS) or id_produto < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found')
    
    # del deleta um determinado elemento da lista pelo seu índice
    del PRODUTOS[id_produto - 1]
    return 

