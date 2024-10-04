from random import shuffle
from time import sleep

loto = list(range(0,61))

print('~~'*5)
print('\33[1:35mMEGA SENA\33[m')
print('~~'*5)

while True:
    resp = 0
    resp = int(input('\n\33[4mEscolha uma opção abaixo\33[m:\n[1] -> JOGO SIMPLES\n[2] -> VARIOS JOGOS\n\n[3] -> SAIR\n: '))
    if resp == 1:
        shuffle(loto)
        print(f'\33[4;36mJOGO\33[m >>> {sorted(loto[0:6])}\n')

    elif resp == 2:
        tot_jogos = int(input('Quantos jogos deseja sortear?: '))
        for n in range(0,tot_jogos):
            shuffle(loto)
            x = sorted(loto[0:6])
            print('\33[4;36mJOGO\33[m')
            print(x)

    elif resp == 3:
        break

    else:
        sleep(1)
        print(f'\33[1;31merro\33[m >>> \33[7m{resp}\33[m Ñ É UMA ENTRADA VALIDA!!, \33[4mresponda apenas com\33[m S \33[4mou\33[m N\n')
        sleep(1)

sleep(2)
print('\n\33[7mOBRIGADO!!!\33[m')