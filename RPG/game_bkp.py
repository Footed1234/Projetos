# tentar separar as funções em arquivos
# mobs para cada bioma
# mob + forte q o ogro
# mob tank (+vida, -atk)
# mob assas (-vida, +atk)
# mini boss com a quest na cidade (nível 15)
# NPC na cidade para a quest (dá mais exp)
# Casa do player na cidade

import tkinter as tk
import random, os
from batalha import batalha
from cura import cura
from save import save, get_save
from loja import compra
from prefeito import prefeito
from caverna import caverna
# from cidade import cidade

run = True
menu = True
jogar = False
chave = "False"
luta = False
afk = True
comprar = False
falar = False
boss = False
fim = "False"

crit = 10
crit_dano = 2
nivel = 1
max_xp = 200
xp = 0
hp = 100
max_hp = 100
atk = 2
pocao = 1
elixir = 0
ouro = 0
x = 0
y = 0

#        x = 0        x = 1        x = 2      x = 3         x = 4       x = 5       x = 6
mapa = [["planície", "planície", "planície", "planície",   "floresta", "montanha", "caverna" ], # y = 0
       ["floresta", "floresta", "floresta", "floresta",   "floresta", "vale",     "montanha"], # y = 1
       ["floresta", "campo",    "ponte",    "planície",   "vale",     "floresta", "vale"    ], # y = 2
       ["planície", "loja",     "cidade",   "prefeitura", "planície", "vale",     "montanha"], # y = 3
       ["planície", "campo",    "campo",    "planície",   "vale",     "montanha", "montanha"]] # y = 4

y_len = len(mapa)-1  # -1 porque tem 5 y mas o primeiro equivale a 0
x_len = len(mapa[0])-1  # -1 porque tem 7 x mas o primeiro equivale a 0

bioma = {
    "planície": {"t": "PLANÍCIE", "e": True},
    "floresta": {"t": "FLORESTA", "e": True},
    "campo": {"t": "CAMPO", "e": False},
    "ponte": {"t": "PONTE", "e": True},
    "cidade": {"t": "CIDADE", "e": False},
    "loja": {"t": "LOJA", "e": False},
    "prefeitura": {"t": "PREFEITURA", "e": False},
    "caverna": {"t": "CAVERNA", "e": True},
    "montanha": {"t": "MONTANHA", "e": True},
    "vale": {"t": "VALE", "e": True}
}

def novo_jogo():
    def escrever_nome():
        # Excluir a janela do certeza
        new.destroy()
        global nome, menu, jogar
        nome = input("-> ")
        menu = False
        jogar = True
        
    # Excluir a janela do menu
    root.destroy()

    # Criar uma nova janela
    new = tk.Tk()
    new.title("Novo Jogo?")
    tk.Label(new, text="Novo jogo?").pack()
    tk.Button(new, text="Sim", command=escrever_nome).pack()
    tk.Button(new, text="Não", command=root.quit).pack()
    new.mainloop()

def carregar_jogo():
    pass

def sair():
    print("Tem certeza que deseja sair? (S ou N)")
    escolha = input("-> ").upper()
    if escolha == "S":
        print("Saindo do jogo...")
        exit()
    else:
        print("Voltando ao menu...")
        return True

def ajuda():
    desenho()
    print("""Guia do cavaleiro!
    1- Você começa na Floresta em 0/0.
    2- O Boss do jogo se localiza na Caverna.
    3- Para lutar contra o Boss você precisa de uma Chave.
    4- A Chave é obtida na Prefeitura com o Prefeito.
    5- Para pegar a Chave você precisa estar no Nível 20.""")
    desenho()
    print("Pressione qualquer botão para voltar ao menu...")
    input()

def clear_screen():
    os.system("cls")  # metodo do OS para limpar a tela

def desenho():
    print("==================")


while run:
    while menu:

        # Criar a janela do menu
        root = tk.Tk()
        root.title("Menu do Jogo")
        tk.Button(root, text="Novo Jogo", command=novo_jogo).pack()
        # tk.Button(root, text="Carregar Jogo", command=carregar_jogo),pack()
        tk.Button(root, text="Ajuda", command=ajuda).pack()
        tk.Button(root, text="Sair do Jogo", command=sair).pack()
        # Iniciar o loop da janela
        root.mainloop()

        # elif escolha == "2":
        #     nome, hp, atk, pocao, elixir, ouro, x, y, chave, fim, xp, nivel, crit, crit_dano, max_hp = get_save()
        #     print(f"Bem-vindo de volta, {nome}!")
        #     print("Pressione qualquer botão para continuar...")
        #     input("-> ")
        #     menu = False
        #     jogar = True

    while jogar:
        save(nome, hp, atk, pocao, elixir, ouro, x, y, chave, fim, xp, nivel, crit, crit_dano, max_hp)  # autosave

        if not afk:
            if bioma[mapa[y][x]]["e"]:
                if random.randint(0, 100) <= 50:
                    hp, pocao, elixir, atk, boss, fim, xp, nivel, max_hp, max_xp, crit, crit_dano = batalha(hp, pocao, elixir, ouro, boss, fim, atk, xp, nivel, max_xp, max_hp, nome, crit, crit_dano)
        clear_screen()
        desenho()
        print("""    x = 0      x = 1      x = 2       x = 3       x = 4      x = 5     x = 6
| planície | planície | planície |  planície  | floresta | montanha | caverna  |  y = 0
| floresta | floresta | floresta |  floresta  | floresta |   vale   | montanha |  y = 1
| floresta |  campo   |  ponte   |  planície  |   vale   | floresta |   vale   |  y = 2
| planície |   loja   |  cidade  | prefeitura | planície |   vale   | montanha |  y = 3
| planície |  campo   |  campo   |  planície  |   vale   | montanha | montanha |  y = 4""")
        desenho()
        print(f"LOCALIZAÇÃO X/Y: {bioma[mapa[y][x]]["t"]} - {x}/{y}")
        desenho()
        print(f"{nome}")
        print(f"HP: {hp} / {max_hp}")
        print(f"ATK: {atk}")
        print(f"POÇÕES: {pocao}")
        print(f"ELIXIRES: {elixir}")
        print(f"NÍVEL: {nivel}")
        print(f"{xp} / {max_xp}")
        print(f"OURO: {ouro}")
        print(f"CRÍTICO: {crit}%")
        print(f"DANO_CRÍTICO: +{crit_dano}")
        if chave == "True":
            print("CHAVE: 1")
        if fim == "True":
            print("ESCAMA DE DRAGÃO (+ 20 ATK)")
        desenho()
        print("0- Salvar e Voltar ao Menu")
        if y > 0:
            print("1- Norte (Y - 1)")
        if x < x_len:
            print("2- Leste (X + 1)")
        if y < y_len:
            print("3- Sul (Y + 1)")
        if x > 0:
            print("4- Oeste(X - 1)")
        if pocao > 0:
            print("5- Usar Poção (+30 HP)")
        if elixir > 0:
            print("6- Usar Elixir (MAX_HP)")
        if mapa[y][x] == "loja" or mapa[y][x] == "prefeitura" or mapa[y][x] == "caverna":
            print("7- Entrar")

        desenho()
        destino = input("-> ")

        if destino == "0":
            jogar = False
            menu = True
            save(nome, hp, atk, pocao, elixir, ouro, x, y, chave, fim, xp, nivel, crit, crit_dano, max_hp)
        elif destino == "1":
            if y > 0:  # se não estiver na borda do mapa
                y -= 1
                afk = False
        elif destino == "2":
            if x < x_len:  # se não estiver na borda do mapa
                x += 1
                afk = False
        elif destino == "3":
            if y < y_len:  # se não estiver na borda do mapa
                y += 1
                afk = False
        elif destino == "4":
            if x > 0:
                x -= 1
                afk = False
        elif destino == "5":
            pocao -= 1
            cura(1, hp, max_hp, nome)
            afk = True
        elif destino == "6":
            elixir -= 1
            cura(2, hp, max_hp, nome)
            afk = True
        elif destino == "7":
            if mapa[y][x] == "loja":
               ouro, pocao, elixir, atk = compra(ouro, pocao, elixir, atk)
            if mapa[y][x] == "prefeitura":
                chave = prefeito(chave, nome, nivel)
            if mapa[y][x] == "caverna":
                boss = True
                caverna(boss, chave, ouro, nome)
        else:
            afk = True
