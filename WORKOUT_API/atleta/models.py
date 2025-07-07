class AtletaModel:
    def __init__(self, id: int, nome: str, idade: int, peso: float, altura: float):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __repr__(self):
        return f"AtletaModel(id={self.id}, nome='{self.nome}', idade={self.idade}, peso={self.peso}, altura={self.altura})"