# DESAFIO 3

# Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo ou não.

# (Um palíndromo é uma palavra que é lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.)

palindromo = input("Digite uma palavra: ")

palindromoInvertida = palindromo[::-1]

if palindromo == palindromoInvertida:
    print ("A palavra é um palíndromo.")
else:
    print ("A palavra não é um palíndromo.")