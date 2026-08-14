import calculadora
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

opcao = int(input('1-Soma 2-Subtração 3-Multiplicação 4-Divisão 5-Sair: '))

if opcao == 1:
    print(calculadora.somar(a, b))