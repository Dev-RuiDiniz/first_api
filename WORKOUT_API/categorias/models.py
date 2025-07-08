from WORKOUT_API.atleta.models import AtletaModel
from contrib.models import ModelBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import List

class CategoriaModel(ModelBase):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    atletas: Mapped[List['AtletaModel']] = relationship('AtletaModel', back_populates='categoria')
