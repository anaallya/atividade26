# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input("Digite o primeiro termo da PA: "))
a2 = int(input("Digite a razão da PA: "))
for l in range(10):
    print(l)
    termo = a1 + l * a2
    print(f'Termo {l+1}: {termo}')