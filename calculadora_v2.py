saida = ''


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return x / y


def calculadora(calc1, calc2, operando):
    if operando == '+' or operando == 'adicao':
        resultcalc = adicao(calc1, calc2)
    elif operando == '-' or operando == 'subtracao':
        resultcalc = subtracao(calc1, calc2)
    elif operando == '*' or operando == 'multiplicacao':
        resultcalc = multiplicacao(calc1, calc2)
    elif operando == '/' or operando == 'divisao':
        resultcalc = divisao(calc1, calc2)
    else:
        resultcalc = 'Operação inválida'
    return resultcalc


while saida.lower() != 'n':
    try:
        num1 = float(input('\nDigite o primeiro número: \n'))
        num2 = float(input('Digite o segundo número: \n'))
        operacao = input('Digite a operação desejada (+, -, *, / ou adicao, subtracao, multiplicacao, divisao): \n')

        resultado = calculadora(num1, num2, operacao)
        print(f'Resultado da operação: {resultado}')

        saida = input('Deseja continuar? (S/N): ')
    except ValueError:
        print('Por favor, digite números válidos.')
