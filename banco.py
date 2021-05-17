from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('-='*10)
    print('-=-=-=- .ATM. -=-=-=')
    print('-=-=-= PyBank -=-=-=')
    print('-='*10)
    print('  Bem vindo PyBank!')
    sleep(0.5)
    print('[1] - Criar Conta.')
    print('[2] - Efetuar Saque.')
    print('[3] - Efetuar Depósito.')
    print('[4] - Efetuar Transferência.')
    print('[5] - Listar Contas.')
    print('[6] - Sair do Sistema.')
    opcao: int = int(input('Seleciona a opção: '))
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Obrigado por utilizar o banco, volte sempre.')
        sleep(0.5)
        exit(0)
    else:
        print('Opção inválida.')
    sleep(0.5)
    menu()


def criar_conta() -> None:
    print('Informe os dados do Cliente!')
    nome: str = input('Nome Completo: ')
    email: str = input('Email do Cliente: ')
    cpf: str = input('Informe seu CPF: ')
    data_nascimento: str = input('Informe sua Data de Nascimento: ')
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)
    sleep(0.5)
    print('Conta criada com sucesso: ')
    print('Dados da conta: ')
    print('-='*10)
    print(conta)
    sleep(0.5)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua Conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta {numero}.')

    else:
        print('Ainda não possuímos contas cadastradas.')
        sleep(0.5)
        menu()
    sleep(0.5)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua Conta: '))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input('Informe o valor do depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta {numero}')
    else:
        print('Ainda não possuímos contas cadastradas.')
        sleep(0.5)
        menu()
    sleep(0.5)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o número da sua Conta: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)
        if conta_origem:
            numero_destino: int = int(input('Informe o número da Conta Destino: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_destino)
            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))
                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'A Conta destino {numero_destino} não foi localizada.')
        else:
            print(f'Não foi encontrada a conta {numero_origem}.')
    else:
        print('Ainda não possuímos contas cadastradas.')
        sleep(0.5)
        menu()
    sleep(0.5)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de Contas!')
        for conta in contas:
            print(conta)
            print('-='*10)
            sleep(0.2)
    else:
        print('Ainda não possuímos contas cadastradas.')
        sleep(0.5)
        menu()
    sleep(0.5)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
