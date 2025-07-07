from contrib.models import ModelBase
from sqlalchemy.orm import Mapped, mapped_column

class AtletaModel(ModelBase):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(integer=True, primary_key=True)
    nome: Mapped[str] = mapped_column(str(50), nullable=False)
    cpf: Mapped[str] = mapped_column(unique=True, nullable=False)  # Unique identifier for the athlete
    idade: Mapped[int] = mapped_column(nullable=False)
    peso: Mapped[float] = mapped_column(nullable=False)
    altura: Mapped[float] = mapped_column(nullable=False)
    sexo: Mapped[str] = mapped_column(nullable=False)  # 'M' or 'F'
    