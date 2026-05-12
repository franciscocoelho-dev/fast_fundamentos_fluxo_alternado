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

class ProdutoUpdateSchema(BaseModel):
    descricao: Optional[str] = None
    quantidade: Optional[int] = None
    valor: Optional[float] = None

class ProdutoListPublicSchema(BaseModel):
    produtos: List[ProdutoPublicSchema]

    