# Vamos testar se uma palavra é um palíndromo?!

# Solicitar a palavra do usuário
palavra = input("Por favor, insira uma palavra: ")

# Remover espaços em branco e converter a palavra para minúsculas
palavra = palavra.replace(" ", "").lower()

# Verificar se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
