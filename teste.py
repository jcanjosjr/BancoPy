from models.cliente import Cliente
from models.conta import Conta

jose: Cliente = Cliente('José Carlos dos Anjos', 'jose@gmail.com', '123.456.789-99', '04/05/1996')
vanessa: Cliente = Cliente('Vanessa Lechuk', 'vanessa@gmail.com', '987.654.321-11', '10/03/1993')

# print(vanessa)
# print(jose)

contaf: Conta = Conta(jose)
contaa: Conta = Conta(vanessa)

# print(contaf)
# print(contaa)
