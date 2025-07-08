from datetime import datetime
from WORKOUT_API.categorias.models import CategoriaModel
from WORKOUT_API.centro_treinamento.models import CentroTreinamentoModel
from contrib.models import ModelBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, Float, DateTime

class AtletaModel(ModelBase):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)  # CPF único
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)  # 'M' ou 'F'
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'), nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atletas')
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'), nullable=False)
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atletas')