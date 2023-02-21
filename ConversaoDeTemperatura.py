celsius = float(input('Informe a temperatura em graus Celsius para realizar a conversão: '))
conv = input('Você gostaria de converter para Kelvin ou Fahrenheit: ')

far = 1.8 * celsius + 32
kelvin = celsius + 273

if conv == 'far':
    print('A conversão de {} graus Celsius para Fahrenheit resulta em {} graus F.'.format(celsius, far))
elif conv == 'kelvin':
    print('A conversão de {} graus Celsius para Kelvin resulta em {} graus K.'.format(celsius, kelvin))

else:
    print('Tente novamente')

