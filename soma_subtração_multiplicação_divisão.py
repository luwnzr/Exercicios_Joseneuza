num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não permitida"

print(f"A soma de {num1} e {num2} é {soma}")
print(f"A subtração de {num1} e {num2} é {subtracao}")
print(f"A multiplicação de {num1} e {num2} é {multiplicacao}")
print(f"A divisão de {num1} por {num2} é {divisao}")
