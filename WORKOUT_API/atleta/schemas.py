from typing import Annotated
from pydantic import Field
from contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', max_length=100)]
    cpf: Annotated[str, Field(description='CPF do Atleta', max_length=11, min_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', ge=0, le=120)]
    peso: Annotated[float, Field(description='Peso do Atleta', ge=0.0)]
    altura: Annotated[float, Field(description='Altura do Atleta', ge=0.0)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', max_length=1, regex='^[MF]$')]
