from time import sleep


print('-'*18)
print('\33[1;36mESTRATEGIA DO GOL!\33[m')
print('-'*18)
sleep(2)

print('Esta estrategia se baseia em avaliar um jogo \33[4mAPARTIR\33[m do minuto 70!!')
sleep(1)
print('Pois a taxa de acerto é maior após esse minuto!\n')
sleep(1)

resp = 0
while resp != 2:
    print('Fazer a analise?')
    resp = int(input('[1]\33[1;32mSIM\33[m\n[2]\33[1;31mNÃO\33[m\n >>: '))

    if resp == 1:
        ataque = int(input('Insira o maior numero de ataques perigosos entre as duas equipes: '))
        tempo = int(input('Coloque o tempo (somente minuto) apartir do minuto 70: '))
        print('\33[1;35mPROCESSANDO\33[m. . . \n')
        sleep(2)
        if tempo < 70 or tempo > 120:
            print('\33[1;31mDADOS INVALIDOS\33[m')
            tempo = int(input('Coloque o tempo (somente minutos) apartir do minuto 70: '))
print('\33[1;35mPROCESSANDO\33[m. . . \n')
sleep(2)

ponto = ataque / tempo

if ponto < 0.98:
    print(f'\33[4mA pontuação do calculo deu {ponto:.2f}, Esta entrada não é muito favoravel\33[m!!\n')

else:
    print(f'\33[4mA pontuação do calculo chegou a {ponto:.2f}, Esta entrada vale a pena ser considerada\33[m!!')
print('ESTA ENTRADA E PARA 1 GOL + NA PARTIDA, para mais gols fica ao seu critério!!!\n')

if resp == 2:
        print('Finalizando programa. . .')
        sleep(2)



print('\33[1;36mFIM DO PROGRAMA\33[m')