# Funções de Operações

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Função principal da calculadora
def calculadora():
    print("Bem-vindo à Calculadora de TI!")
    print("Escolha a operação que deseja realizar:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    # Verificando se a entrada é válida
    if escolha not in ['1', '2', '3', '4']:
        print("Escolha inválida!")
        return

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"O resultado é: {somar(num1, num2)}")
    elif escolha == '2':
        print(f"O resultado é: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"O resultado é: {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"O resultado é: {dividir(num1, num2)}")

# Executando a calculadora
calculadora()
