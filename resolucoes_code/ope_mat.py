# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitar os números do usuário
numero1 = float(input("Por favor, insira o primeiro número: "))
numero2 = float(input("Por favor, insira o segundo número: "))

# Solicitar a operação do usuário
operacao = input("Por favor, escolha a operação (+, -, *, /): ")

# Realizar a operação escolhida
if operacao == "+":
    resultado = numero1 + numero2
    print("A soma dos números é:", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("A subtração dos números é:", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("O produto dos números é:", resultado)
elif operacao == "/":
    # Verificar se o divisor é zero
    if numero2 != 0:
        resultado = numero1 / numero2
        print("A divisão dos números é:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma operação válida (+, -, *, /).")
