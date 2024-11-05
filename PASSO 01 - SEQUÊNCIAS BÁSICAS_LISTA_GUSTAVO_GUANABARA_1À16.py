"""Questão 1"""
print("Olá, Mundo!")

"""Questão 2"""
nome = input("Qual é o seu nome? ")
print(f"Olá {nome}, é um prazer te conhecer!")

"""Questão 3"""
nome = input("Nome do Funcionário: ")
salario = float(input("Salário: "))
print(f"O funcionário {nome} tem um salário de R${salario:.2f} em Junho.")

"""Questão 4"""
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
soma = valor1 + valor2
print(f"A soma entre {valor1} e {valor2} é igual a {soma}.")

"""Questão 5"""
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
print(f"A média entre {nota1} e {nota2} é igual a {media:.1f}")

"""Questão 6"""
numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"O antecessor de {numero} é {antecessor}")
print(f"O sucessor de {numero} é {sucessor}")

"""Questão 7"""
numero = float(input("Digite um número: "))
dobro = numero * 2
terca_parte = numero / 3
print(f"O dobro de {numero} é {dobro}")
print(f"A terça parte de {numero} é {terca_parte:.5f}")

"""Questão 8"""
metros = float(input("Digite uma distância em metros: "))
print(f"A distância de {metros}m corresponde a:")
print(f"{metros / 1000} Km")
print(f"{metros / 100} Hm")
print(f"{metros / 10} Dam")
print(f"{metros * 10} dm")
print(f"{metros * 100} cm")
print(f"{metros * 1000} mm")

"""Questão 9"""
reais = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = reais / 3.45
print(f"Com R${reais:.2f} você pode comprar US${dolar:.2f}")

"""Questão 10"""
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
tinta = area / 2
print(f"A área da parede é {area} m² e você precisará de {tinta:.1f} litros de tinta.")

"""Questão 11"""
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
delta = b**2 - 4 * a * c
print(f"O valor de Delta é {delta}")

"""Questão 12"""
preco = float(input("Digite o preço do produto: R$"))
desconto = preco * 0.05
preco_promocional = preco - desconto
print(f"O preço promocional com 5% de desconto é R${preco_promocional:.2f}")

"""Questão 13"""
salario = float(input("Digite o salário do funcionário: R$"))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O novo salário com 15% de aumento é R${novo_salario:.2f}")

"""Questão 14"""
km_percorridos = float(input("Quantos Km foram percorridos? "))
dias_alugados = int(input("Por quantos dias o carro foi alugado? "))
preco_total = (dias_alugados * 90) + (km_percorridos * 0.20)
print(f"O preço total a pagar é R${preco_total:.2f}")

"""Questão 15"""
dias_trabalhados = int(input("Quantos dias foram trabalhados no mês? "))
horas_por_dia = 8
salario_por_hora = 25
salario_mensal = dias_trabalhados * horas_por_dia * salario_por_hora
print(f"O salário mensal é R${salario_mensal:.2f}")

"""Questão 16"""
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

# Calculando a perda total de tempo em minutos
tempo_perdido_minutos = cigarros_por_dia * 10 * 365 * anos_fumando
tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)
print(f"Você perdeu aproximadamente {tempo_perdido_dias:.1f} dias de vida devido ao fumo.")
