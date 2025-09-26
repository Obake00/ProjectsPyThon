# faca um programa que peca 3 numeros inteiros e mostre na tela o menor e o maior entre eles.

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} eh o maior')
elif n2 > n1 and n2 > n3:
    print(f'{n2} eh o maior')
else:
    print(f'{n3} eh o maior')    

if n1 < n2 and n1 < n3:
    print(f'{n1} eh o menor')
elif n2 < n1 and n2 < n3:
    print(f'{n2} eh o menor')
else:
    print(f'{n3} eh o menor')