import os

def clear_screen():
    os.system("cls")  # metodo do OS para limpar a tela

def desenho():
    print("==================")

def prefeito(chave, nome, nivel):

    falar = True

    while falar:
        clear_screen()
        desenho()
        print(f"Olá, {nome}!")
        if nivel < 25:
            print("Você não tem poder o suficiente para enfrentar o dragão. Continue sua jornada e volte quando alcançar o nível 25!")
            chave = "False"
        else:
            print("Parabéns! Você já é capaz de enfrentar o dragão! Pegue essa chave, mas tome cuidado!")
            chave = "True"

        desenho()
        print("1- Sair")
        desenho()

        escolha = input("-> ")

        if escolha == "1":
            falar = False
            return chave