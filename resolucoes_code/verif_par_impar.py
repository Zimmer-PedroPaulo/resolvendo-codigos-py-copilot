# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

# Solicitar o número inteiro do usuário
numero = int(input("Por favor, insira um número inteiro: "))

# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
