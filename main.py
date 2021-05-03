from typing import List,Dict
from time import sleep
import uuid

from Utilitario.helper import formataMoeda
from Classe.cliente import Cliente
from Classe.produto import Produto


clientes  = []
produtos  = []
pedidos = []




def main() -> None:
    menu()


def menu() -> None:
    print('===================================')
    print('=========== Bem-vindo(a) ==========')
    print('==============  NOC  ==============')
    print('===================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cliente')
    print('2 - Produtos')
    print('3 - Pedidos')
    print('4 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        menuCliente()
    elif opcao == 2:
        menuProduto()
    elif opcao == 3:
        menuPedido()
    elif opcao == 4:
        print('Volte sempre!')
        sleep(1)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()
#começo funções menu cliente
def menuCliente():
    print('======================================')
    print('=========== Area do Cliente ==========')
    print('==============  NOC  =================')
    print('======================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastro cliente')
    print('2 - Atualizar dados cliente')
    print('3 - Excluir cliente')
    print('4 - voltar')

    opcao: int = int(input())

    if opcao == 1:
        cadastroCliente()
    elif opcao == 2:
        atualizarCliente()
    elif opcao == 3:
        excluirCliente()
    elif opcao == 4:
        sleep(1)
        menu()
    else:
        print('Opção inválida!')
        sleep(1)
        menuCliente()
def cadastroCliente() -> None:
        nome: str = input('Digite o nome do cliente:')
        telefone: str = input('Digite o numero de telefone do cliente: ')
        cpf: str = input('Digite o CPF: ')

        cliente: Cliente = Cliente (nome, telefone, cpf)
        clientes.append(cliente)
        print(clientes)

        sleep(1)
        menuCliente()

def atualizarCliente() -> None:
    if len(clientes) > 0:
        print('-----------------------------------------------------')
        print(list(map(lambda c: (c.nome, c.codigo), clientes)))

        sleep(1)
        codigo = input('Digite o codigo do cliente')
        cliente: Cliente = buscarCliente(clientes, codigo)

        cliente.nome = str(input(f'Digite o nome do cliente'))
        cliente.telefone = str(input('Digite o telefone do cliente:'))

        print(cliente)
        sleep(1)
        menuCliente()

    else:
     print('Ainda não existe clientes cadastrados.')
     sleep(1)
     menuCliente()

def excluirCliente() -> None:
    if len(clientes) > 0:
        print('-----------------------------------------------------')
        print(list(map(lambda c: (c.nome, c.codigo), clientes)))
        sleep(1)

        codigo = input('Digite o codigo do cliente que deseja excluir: ')
        cliente: Cliente = buscarCliente(clientes, codigo)

        clientes.remove(cliente)

        print('Cliente excluido com sucesso')
        sleep(1)
        menuCliente()
    else:
        print('Ainda não existem clientes parar serem excluidos')


def buscarCliente(clientes, codigo ):
    return next(filter(lambda c: c.codigo == codigo, clientes), None)

#Fim funções menu cliente

#Começo funções menu produto
def menuProduto():
    print('======================================')
    print('=========== Area do Produto ==========')
    print('==============  NOC  =================')
    print('======================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastro produto')
    print('2 - Atualizar dados produto')
    print('3 - Excluir produto')
    print('4 - Voltar')

    opcao: int = int(input())

    if opcao == 1:
        cadastroProduto()
    elif opcao == 2:
        atualizarProduto()
    elif opcao == 3:
        excluirProduto()
    elif opcao == 4:
        sleep(1)
        menu()
    else:
        print('Opção inválida!')
        sleep(1)
        menu()

def cadastroProduto() -> None:
        print('Informe os dados do produto: ')

        nome: str = input('Digite o nome do produto:')
        preco: float = float(input('Digite o valor do produto: '))

        produto: Produto = Produto(nome, preco)

        produtos.append(produto)
        print('Produto cadastrado com sucesso!')
        print(f'''Dados produto:
            ==================================
            Nome: {produto.nome}
            Preço: {formataMoeda(produto.preco)}        
               ''')
        sleep(1)
        menuProduto()

def atualizarProduto():
    if len(produtos) > 0:
        print('-----------------------------')
        print(list(map(lambda p: (p.codigo, p.nome, p.preco ) , produtos)))
        sleep(1)

        codigo = input('Insira o codigo: ')
        produto: Produto = buscarCodigo(produtos, codigo)

        produto.nome = str(input(f'Digite o nome do produto: '))
        produto.preco = float(input('Digite o preço: '))

        print(produto)
        sleep(1)
        menuProduto()

    else:
        print('Ainda não há produtos cadastrados')
        sleep(1)
        menuProduto()

def excluirProduto():
    if len(produtos) > 0:
        print('------------------------')
        print(list(map(lambda p: (p.codigo, p.nome), produtos)))
        sleep(1)

        codigo = input('Digite o codigo do produto que deseja excluir: ')
        produto: Produto = buscarCodigo(produtos, codigo)

        produtos.remove(produto)

        print('Produto excluido com sucesso!')
        sleep(1)
        menuProduto()
    else:
        print('Ainda não existem produtos para serem excluidos')

def buscarCodigo(produtos, codigo):
    return next(filter(lambda p: p.codigo == codigo, produtos), None)

#Fim funções produto

#Começo funções pedido
def menuPedido():
    print('======================================')
    print('============= Pedidos ================')
    print('==============  NOC  =================')
    print('======================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Realizar pedido')
    print('2 - Atualizar dados pedido')
    print('3 - Excluir pedido')
    print('4 - Fechar pedido')
    print('5 - Voltar')

    opcao: int = int(input())

    if opcao == 1:
        realizarPedido()
    elif opcao == 2:
        atualizarPedido()
    elif opcao == 3:
        excluirPedido()
    elif opcao == 4:
        fecharPedido()
    elif opcao == 5:
        sleep(1)
        menu()
    else:
        print('Opção inválida!')
        sleep(1)
        menu()
def realizarPedido():
    if len(produtos) > 0:
        print('Informe o codigo do cliente: ')
        print('--------------------------------------------------------------')
        print('--------------------------------------------------------------')
        print(list(map(lambda c: (c.codigo, c.nome), clientes)))

        codigo = input()
        cliente: Cliente = buscarCliente(clientes, codigo)


        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('--------------------------------------------------------------')
        print(list(map(lambda p: (p.codigo, p.nome, p.preco), produtos)))
        sleep(1)

        codigo = input()
        produto: Produto = buscarCodigo(produtos, codigo)

        pedido = ((produto.codigo,produto.nome, produto.preco) + (cliente.codigo,cliente.nome))

        pedidos.extend(pedido)
        print(pedido)
        sleep(1)
        menuPedido()
    else:
        ('Não a produtos para sempre colocados no pedido')


    pass
def atualizarPedido():
    if len(pedidos) > 0:
        print(list(map(lambda pd: (pd.codigo, pd.preco), produtos)))
        sleep(1)


    else:
        print('Não há pedidos.')
def excluirPedido():
    pass

def fecharPedido() -> None:
    if len(pedidos) > 0:
        valor_total: float = 0

        print('Produtos em pedido')
        produtoPed = [produto for produto in produtos if produto > 0]

        print(produtoPed)

        print(f'Sua fatura é {formataMoeda(valor_total)}')
        print('Volte sempre!')
        pedidos.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(1)
    menuPedido()



def buscarPedido(pedidos, codigo):
    return next(filter(lambda p: p.codigo == codigo, pedidos), None)

#Fim funções pedido


if __name__ == '__main__':
    main()