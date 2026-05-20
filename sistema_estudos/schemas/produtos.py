from pydantic import BaseModel
from typing import Optional, List

# Entrada de dados de um produto
class ProdutoSchema(BaseModel):
    descricao: str
    quantidade: int
    valor: float

# Os campos de retorno de um produto (consulta)
class ProdutoPublicSchema(BaseModel):
    id: int
    descricao: str
    quantidade: int
    valor: float

# É usado Optional pelo fato dos campos serem opcionais a edição, o usuário pode editar apenas um campo (exemplo).
class ProdutoUpdateSchema(BaseModel):
    descricao: Optional[str] = None
    quantidade: Optional[int] = None
    valor: Optional[float] = None

# Cria o esquema de retorno de uma lista com todos os produtos
class ProdutoListPublicSchema(BaseModel):
    produtos: List[ProdutoPublicSchema]

    