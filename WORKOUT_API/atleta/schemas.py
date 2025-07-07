from pydantic import Field
from contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: str = Field(description='Nome do Atleta', max_length=100)
    cpf:  str = Field(description='CPF do Atleta', max_length=11, min_length=11)
    idade: int = Field(description='Idade do Atleta', ge=0, le=120)
    peso: float = Field(description='Peso do Atleta', ge=0.0)
    altura: float = Field(description='Altura do Atleta', ge=0.0)
    sexo: str = Field(description='Sexo do Atleta', max_length=1, regex='^[MF]$')
    