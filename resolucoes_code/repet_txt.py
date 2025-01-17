# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitar a string do usuário
string = input("Por favor, insira uma string: ")

# Solicitar o número inteiro do usuário
numero = int(input("Por favor, insira um número inteiro: "))

# Repetir a string o número de vezes informado
resultado = (string + ' ') * (numero - 1) + string + '.'

# Exibir o resultado
print("A string repetida é:", resultado)
