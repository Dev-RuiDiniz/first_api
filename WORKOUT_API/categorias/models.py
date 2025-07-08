from contrib.models import ModelBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class CategoriaModel(ModelBase):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
