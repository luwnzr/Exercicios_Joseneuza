"""Criar um programa que leia peso e altura e calcule o IMC"""

peso = float(input("Digite o peso"))
altura = float(input("Digite a altura"))
imc = peso / (altura ** 2)
print(f"O valor do IMC {imc}")
