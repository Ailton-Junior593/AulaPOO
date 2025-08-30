# # nome = 'Felipe'

# # lista = []


# # class Carro:
# #     def __init__(self, qtd_portas: int, cor: str, modelo: str, ano: int):
# #         self.qtd_portas = qtd_portas
# #         self.cor = cor
# #         self.modelo = modelo
# #         self.ano = ano


# # carro1 = Carro(4, 'Azul', 'Uno', 2005)

# # print(carro1.qtd_portas)
# # print(carro1.ano)


# # print(carro1.__dict__)

# # print(type(carro1))

# class Pessoa:
#     def __init__(self,conta: str, qtd_dinheiro: float, agencia: str,nome: str, cpf: int, rg: str):
#         self.conta = conta
#         self.qtd_dinheiro = qtd_dinheiro
#         self.agencia = agencia
#         self.nome = nome
#         self.cpf = cpf
#         self.rg = rg



# # pessoa1 = Pessoa('0000', 400.00, 'Itau', 'Ailton', 000000000, '45821561255')

# # print(pessoa1.__dict__)




# class ContaCorrente:
#     def __init__(self,agencia: int, numero: int):
#         self.agencia = agencia
#         self.numero = numero
#         self.saldo = 0
#         self.credito = 0

    
#     def depositar(self, valor: float):
#         self.saldo += valor
        
#     def adicionar_credito(self, valor):
#         self.credito += valor
        
#     def sacar(self, valor):
#         if self.saldo >= valor:
#             self.saldo -= valor
#         else:
#             return 'Saldo insuficiente para saque'
        

#     def transferencia(self, valor, conta):
#         if self.saldo <= 0:
#             return 'Saldo insuficiente para realizar a transferencia'
#         elif self.saldo >= valor:
#             self.saldo -= valor
#             conta.saldo += valor




# class ContaPoupanca:
#     def __init__(self,agencia: str, numero: int):
#           self.agencia = agencia
#           self.numero = numero
#           self.saldo = 0
        

#     def depositar(self, valor: float):
#         self.saldo += valor

#     def sacar(self, valor):
#         if self.saldo >= valor:
#             self.saldo -= valor
#         else:
#             return 'Saldo insuficiente para saque'
        
   
        


# conta1 = ContaCorrente(1234, 369852147)

# conta2 = ContaPoupanca(5432, 258741369)

# conta1.depositar(1000)

# print(conta1.__dict__)
# print(conta2.__dict__)

# conta1.transferencia(500, conta2)


# print(conta1.__dict__)
# print(conta2.__dict__)

# contap = ContaPoupanca(9876, 369741258)

# conta1.transferencia(100, contap)

# print(conta1.__dict__)
# print(contap.__dict__)