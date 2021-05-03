from Utilitario.helper import formataMoeda
import uuid

class Produto(object):
    codigo = ''
    nome = ''
    preco = ''

    def __init__(self, nome, preco):
        self.codigo = str(uuid.uuid4())
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {self.preco}'

