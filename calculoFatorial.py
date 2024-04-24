# DESAFIO 4

# Crie um programa que solicita ao usuário que insira um número inteiro positivo e, em seguida, calcula e exibe o fatorial desse número.

# (O fatorial de um número é o produto de todos os números inteiros positivos de 1 até o próprio número.)

import math

i = int(input("Insira um numero inteiro positivo: "))
if i > 0:
    j = math.factorial(i)
    print("O fatorial de", i, "é", j)
else:
    print("Número Inválido!")
