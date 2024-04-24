# DESAFIO 5

# Crie um programa que permita ao usuário gerenciar suas tarefas diárias. O programa deve oferecer as seguintes funcionalidades:

# Adicionar uma nova tarefa;
# Visualizar todas as tarefas;
# Marcar uma tarefa como concluída;
# Remover uma tarefa;
# Sair do programa.
# (Você pode implementar essas funcionalidades usando listas para armazenar as tarefas e estruturas de controle como loops e condicionais para interagir com o usuário.)


menu = """
[1] - Adicionar tarefa 
[2] - Visualizar todas as tarefas
[3] - Atualizar tarefa
[4] - Remover tarefa
[0] - Sair 
"""
listaTarefas = []
tarefa = ""
i = 0



while True:

    opcao = int(input(menu))
    if opcao == 1:
        # Adicionar tarefa 
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        listaTarefas.append(tarefa)

    elif opcao == 2:
        # Visualizar todas as tarefas
        print("Lista de tarefas:\nId | Tarefa")
        for i, tarefa in enumerate(listaTarefas):
            print(i , " | " , tarefa)
    elif opcao == 3:
        # Atualizar tarefa
        print("Lista de tarefas:\nId | Tarefa")
        for i, tarefa in enumerate(listaTarefas):
            print(i , " | " , tarefa)

        id = int(input("Digite o id da tarefa que deseja atualizar: "))
        del(listaTarefas[id])
        novatarefa = input("Digite a atualização: ")
        listaTarefas.insert(id, novatarefa)
        print("Tarefa Atualizada!\n")
        print("Lista de tarefas atualizada:\nId | Tarefa")
        for i, tarefa in enumerate(listaTarefas):
            print(i , " | " , tarefa)
    elif opcao == 4:
        # Remover tarefa
        print("Lista de tarefas:\nId | Tarefa")
        for i, tarefa in enumerate(listaTarefas):
            print(i , " | " , tarefa)
        id = int(input("Digite o id da tarefa que deseja remover: "))
        del(listaTarefas[id])
        print("Tarefa Removida!\n")
        print("Lista de tarefas atualizada:\nId | Tarefa")
        for i, tarefa in enumerate(listaTarefas):
            print(i , " | " , tarefa)
    elif opcao == 0:
        break
    else:
        print("Operação inválida!\n")