from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from sistema_estudos.models.base import Base
from datetime import datetime

class Produto(Base):
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(primary_key=True)
    descricao: Mapped[str] = mapped_column(unique=True)
    quantidade: Mapped[int]
    valor: Mapped[float]
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(), server_default=func.now()
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )

 