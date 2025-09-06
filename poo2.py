# class Pessoa:
#     def __init__(self, idade, nome):
#         self.idade = idade
#         self.nome = nome
#     def locomover(self):
#         print(f'{self.nome} caminha')


# class Jogador(Pessoa):
#     def __init__(self, idade, nome, velocidade, f_chute, precisao):
#         super().__init__(idade, nome)
#         self.velocidade = velocidade
#         self.f_chute = f_chute
#         self.precisao = precisao

#     def locomover(self):
#         print(f'{self.nome} corre')
  

# class Goleiro(Jogador):
#     def __init__(self, idade, nome, velocidade, f_chute, precisao, envergadura):
#         super().__init__(idade, nome, velocidade, f_chute, precisao)
#         self.envergadura = envergadura



# # Neymar = Jogador(32,'Neymar', 12, 88, 88)

# # print(Neymar.__dict__)
# # Neymar.locomover()

# Dida = Goleiro(45, 'Dida', 8, 70, 90, 1.90)

# print(Dida.__dict__)

# Exercicio 1

# class Forma():
#     def __init__(self, base, altura,):
#         self.base = base
#         self.altura = altura

    
        

# class Retangulo(Forma):
#     def __init__(self, base, altura):
#         super().__init__(base, altura)

#     def CalcularArea(self):
#         area = self.altura * self.base
#         return area
    
#     def CalcularPerimetro(self):
#         perimetro = self.altura*2 + self.base*2
#         return perimetro
        
    
# class Circulo(Forma):
#     def __init__(self, base, altura):
#         super().__init__(base, altura)

#     def CalcularArea(self):
#         area = (self.base/2)**2*3.14
#         return area
    
#     def CalcularPerimetro(self):
#         perimetro = 2*3.14*(self.base/2)
#         return perimetro



# retangulo = Retangulo(8, 16)

# print(retangulo.CalcularArea())
# print(retangulo.CalcularPerimetro())


# circulo = Circulo(7,7)

# print(circulo.CalcularArea())
# print(circulo.CalcularPerimetro())


#Exercicio 2

# class Veiculo:
#     def __init__(self, cor, modelo, n_rodas):
#         self.cor = cor
#         self.modelo = modelo
#         self.n_rodas = n_rodas

#     def trocar_cor(self, nova_cor):
#         self.cor = nova_cor
#         print(f"A cor do veiculo foi trocada para {self.cor}.")

# class Bicicleta(Veiculo):
#     def __init__(self, cor, modelo, n_rodas):
#         super().__init__(cor, modelo, n_rodas)

# class Carro(Veiculo):
#     def __init__(self, cor, modelo, n_rodas):
#         super().__init__(cor, modelo, n_rodas)

# monark = Bicicleta("Vermelha", "Trabalho", 2)
# print(monark.__dict__)

# monark.trocar_cor("Azul")