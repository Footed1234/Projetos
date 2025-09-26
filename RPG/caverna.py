from batalha import batalha
import os

def clear_screen():
    os.system("cls")  # metodo do OS para limpar a tela

def desenho():
    print("==================")

def caverna(boss, chave, ouro, nome):

    boss = True

    while boss:
        clear_screen()
        desenho()
        print("Essa é a caverna do dragão. O que deseja fazer?")
        desenho()
        if chave == "True":
            print("1- Usar a chave")
        print("2- Sair")
        desenho()

        escolha = input("-> ")

        if escolha == "1":
            hp, pocao, elixir, atk, boss, fim, xp, nivel, max_hp, max_xp, crit, crit_dano = batalha(hp, pocao, elixir, ouro, boss, fim, atk, xp, nivel, max_xp, max_hp, nome, crit, crit_dano)
        elif escolha == "2":
            boss = False