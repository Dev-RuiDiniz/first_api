from datetime import datetime
from contrib.models import ModelBase
from sqlalchemy.orm import Mapped, mapped_column

class AtletaModel(ModelBase):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(integer=True, primary_key=True)
    nome: Mapped[str] = mapped_column(str(50), nullable=False)
    cpf: Mapped[str] = mapped_column(str(11), unique=True, nullable=False)  # Unique identifier for the athlete
    idade: Mapped[int] = mapped_column(integer=True, nullable=False)
    peso: Mapped[float] = mapped_column(float, nullable=False)
    altura: Mapped[float] = mapped_column(float, nullable=False)
    sexo: Mapped[str] = mapped_column(str(1), nullable=False)  # 'M' or 'F'
    created_at: Mapped[datetime] = mapped_column(datetime, nullable=False)