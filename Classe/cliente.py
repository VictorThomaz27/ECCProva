import uuid

class Cliente(object):
    codigo = ''
    nome = ''
    cpf = ''
    telefone = ''

    def __init__(self, nome, telefone,cpf):
        self.codigo = str (uuid.uuid4())
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \n Telefone: {self.telefone} \nCpf: {self.cpf}'

