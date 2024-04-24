# Crie um programa que solicita ao usuário que insira três notas 
# (valores de 0 a 10) e, em seguida, calcule e exiba a média dessas notas.

# Além disso, informe ao usuário se ele foi aprovado ou reprovado 
# com base na média das notas, considerando a média mínima de aprovação como 6.

notas = []
media: float = 0
i = 3
soma = 0
todasNotas = True


while todasNotas:
  for nota in range(i):
    notaInserida = float(input("Insira o valor da nota: "))
    if notaInserida >= 0 and notaInserida <= 10:
      notas.append(notaInserida)
      if len(notas) == 3:
        soma = sum(notas)
        media = soma / len(notas)
        if media > 5:
          print(f"O aluno foi aprovado com media: {media:.2f}")
        else:
          print(f"O aluno foi reprovado com media: {media:.2f}")
          todasNotas = False
    else:
      print("Nota inválida! Insira um valor de 0 a 10. ")
