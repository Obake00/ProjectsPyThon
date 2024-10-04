import os

print('\33[4;34m=-= Calculo IMC =-=\33[m\n')
altura = float(input('insira a altura: '))
peso = float(input('insira seu peso: '))


imc = peso / altura ** 2
print('\nSeu IMC esta em: {:.1f}\n'.format(imc))

if imc < 18.5:
    print('\33[1;34mVoce esta abaixo do peso!!\33[m')
elif imc >= 18.5 and imc <= 25:
    print('\33[1;32mVoce esta na faixa de peso ideal!\33[m')
elif imc > 25 and imc <= 30:
    print('\33[1;31mCuidado! Voce esta com sobre-peso!!!\33[m')
elif imc > 30 and imc <= 40:
    print('\33[1;35mVoce esta com OBESIDADE!!\33[m')
else:
    print('\33[30:41mVOCE ESTA COM OBESIDADE MORBIDA !!!\33[m')

os.system('pause')