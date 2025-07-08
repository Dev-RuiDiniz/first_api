from pydantic import Field
from contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: str = Field(description='Nome da Categoria', max_length=10)