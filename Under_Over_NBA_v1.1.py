from time import sleep
import os

frase_feitos = ('Insira o placar de pontos \33[1;32mFEITOS\33[m pela equipe!\n')
frase_sofridos = ('Insira o placar de pontos \33[1;31mSOFRIDOS\33[m pela equipe!\n')
pro = ('\33[1;35mPROCESSANDO\33[m. . .\n')


print('-=-=-= \33[1;36mCalculo OVER/UNDER para NBA\33[m =-=-=-\n')
sleep(2)
print('\33[4mEscolha uma das opções abaixo:\33[m')
sleep(1)

resp = 0
while resp != 3:
    print('[1] >> Média de pontos\n[2] >> Apostas para OVER ou UNDER\n[3] >> Sair ')
    resp = int(input('Digite a opção: '))
    if resp == 1:
        print('\nPara esta opção, tenha os 4 ultimos jogos e pontuações positivas e negativas do time!')
        print(frase_feitos)

        pf1 = int(input('Primeira jogo: '))
        pf2 = int(input('Segunda jogo: '))
        pf3 = int(input('Terceiro jogo: '))
        pf4 = int(input('Quarto jogo: '))
        print(pro)
        sleep(2)
        print(frase_sofridos)
        ps1 = int(input('Primeiro jogo: '))
        ps2 = int(input('Segundo jogo: '))
        ps3 = int(input('Terceiro jogo: '))
        ps4 = int(input('Quarto jogo: '))

        media_pos = (pf1 + pf2 + pf3 + pf4)/4
        media_neg = (ps1 + ps2 + ps3 + ps4)/4

        print(pro)
        sleep(3)
        print(f'\33[4mA media de pontos feitos pela equipe é {media_pos:.1f} e de pontos sofridos é {media_neg:.1f}\33[m\n')
        sleep(3)

    elif resp == 2:
        print('\33[4mPara este calculo, preciso que voce tenha os 4 ultimos jogos dos 2 times a serem avaliados\33[m!!\n')
        print(frase_feitos, 'A')
        pfa1 = int(input('Primeiro jogo: '))
        pfa2 = int(input('Segundo jogo: '))
        pfa3 = int(input('Terceiro jogo: '))
        pfa4 = int(input('Quarto jogo: '))
        print(pro)
        sleep(2)

        print(frase_sofridos, 'A')
        psa1 = int(input('Primeiro jogo: '))
        psa2 = int(input('Segundo jogo: '))
        psa3 = int(input('Terceiro jogo: '))
        psa4 = int(input('Quarto jogo: '))
        print(pro)
        sleep(2)

        print(frase_feitos, 'B')
        pfb1 = int(input('Primeiro jogo: '))
        pfb2 = int(input('Segundo jogo: '))
        pfb3 = int(input('Terceiro jogo: '))
        pfb4 = int(input('Quarto jogo: '))
        print(pro)
        sleep(2)

        print(frase_sofridos, 'B')
        psb1 = int(input('Primeiro jogo: '))
        psb2 = int(input('Segundo jogo: '))
        psb3 = int(input('Terceiro jogo: '))
        psb4 = int(input('Quarto jogo: '))

        media_pos1a = (pfa1 + pfa2 + pfa3 + pfa4) / 4
        media_neg1a = (psa1 + psa2 + psa3 + psa4) / 4
        media_pos2b = (pfb1 + pfb2 + pfb3 + pfb4) / 4
        media_neg2b = (psb1 + psb2 + psb3 + psb4) / 4

        media_final = (media_pos1a + media_neg1a + media_pos2b + media_neg2b)/2
        print(pro)
        sleep(2)
        print(pro)
        sleep(2)
        print(f'\33[4mO resultado da verificação dos 2 times, retorna uma linha de entrada em torno de\33[m >>> {media_final:.1f}\n')
        sleep(3)

    if resp == 3:
        print('\33[1;36mFinalizando o programa\33[m. . .')
    else:
        print('\n\33[4;31mOPÇÃO INVALIDA!!\33[m, escolha conforme a tabela!!')
print('\n-=-=-= \33[1;36mFIM DO PROGRAMA\33[m =-=-=-')

os.system('pause')