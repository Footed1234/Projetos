# mobs para cada bioma
# mob + forte q o ogro
# mob tank (+vida, -atk)
# mob assas (-vida, +atk)
# mini boss com a quest na cidade (nível 15)
# NPC na cidade para a quest (dá mais exp)
# Casa do player na cidade
# Janela para Caverna e Prefeitura
# colocar os ataques em sequência: aparece o seu, depois aparece o do inimigo

from tkinter import *
import random
import estado as est
from novo_jogo import novo_jogo
from carregar_jogo import carregar_jogo
from ajuda import ajuda
from sair_jogo import sair
from batalha import batalha
from cura import cura
from save import save
from loja import compra
from prefeito import prefeito
from caverna import caverna
# from cidade import cidade

#        x = 0        x = 1        x = 2      x = 3         x = 4       x = 5       x = 6
mapa = [["planície", "planície", "planície", "planície", "floresta", "montanha", "caverna" ], # y = 0
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

if est.run:
    while est.menu:
        
        def abrir_menu():
            m3nu = Tk()
            m3nu.title("Menu do Jogo")
            m3nu.attributes('-fullscreen', True)
             # Cria um Frame/Tabela para os botões
            larg_bt_m3nu = 20
            botoes_frame = Frame(m3nu)
            botoes_frame.pack(expand=True, anchor="center")
            m3nu.grid_columnconfigure(0, weight=1)
            m3nu.grid_rowconfigure(0, weight=1)
            for _ in range(2):
                botoes_frame.grid_columnconfigure(_, weight=0)
                botoes_frame.grid_rowconfigure(_, weight=0)
            Button(botoes_frame, text="NOVO JOGO", command=lambda: novo_jogo(m3nu), width=larg_bt_m3nu, font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5)
            Button(botoes_frame, text="CARREGAR JOGO", command=lambda: carregar_jogo(m3nu), width=larg_bt_m3nu, font=("Arial", 10)).grid(column=1, row=0, padx=5, pady=5)
            Button(botoes_frame, text="AJUDA", command=lambda: ajuda(m3nu), width=larg_bt_m3nu, font=("Arial", 10)).grid(column=0, row=1, padx=5, pady=5)
            Button(botoes_frame, text="SAIR DO JOGO", command=lambda: sair(m3nu), width=larg_bt_m3nu, font=("Arial", 10)).grid(column=1, row=1, padx=5, pady=5)
            m3nu.mainloop()
        
        abrir_menu()
        
    if est.jogar:

        def limpar_curou():
            curou.config(text="")

        def checar_batalha():
            if not est.afk:
                if bioma[mapa[est.y][est.x]]["e"]:
                    if random.randint(0, 100) <= 70:
                        batalha(game, atualizar_mapa, curou)
        
        def gerar_mapa():
            mapa_formatado = ""
            for y, linha in enumerate(mapa):
                linha_formatada = ""
                for x, terreno in enumerate(linha):
                    if x == est.x and y == est.y:
                        linha_formatada += f"[{terreno.upper()}] ".ljust(12)  # Destaca a posição do jogador
                    else:
                        linha_formatada += f"{terreno} ".ljust(12)
                mapa_formatado += linha_formatada.rstrip()
                if y < len(mapa) - 1:
                    mapa_formatado += "\n"
            return mapa_formatado
        
        def atualizar_mapa():
            novo_mapa = gerar_mapa()
            mapa_label.config(text=novo_mapa)
            novo_perfil = f"""==================
LOCALIZAÇÃO X/Y: {bioma[mapa[est.y][est.x]]["t"]} - {est.x}/{est.y}
==================
{est.nome}
HP: {est.hp} / {est.max_hp}
ATK: {est.atk}
POÇÕES: {est.pocao}
ELIXIRES: {est.elixir}
NÍVEL: {est.nivel}
{est.xp} / {est.max_xp}
OURO: {est.ouro}
CRÍTICO: {est.crit}%
DANO_CRÍTICO: +{est.crit_dano}"""
            mo_perfil.config(text=novo_perfil)
            save(est.nome, est.hp, est.atk, est.pocao, est.elixir, est.ouro, est.x, est.y, est.chave, est.fim, est.xp, est.nivel, est.crit, est.crit_dano, est.max_hp, est.max_xp)  # autosave

        def voltar():
            game.destroy()
            est.jogar = False
            est.menu = True
            est.afk = True
            abrir_menu()

        def Norte():
            limpar_curou()
            if est.y > 0:
                est.y -= 1
                est.afk = False
                atualizar_mapa()
                checar_batalha()

        def Leste():
            limpar_curou()
            if est.x < x_len:
                est.x += 1
                est.afk = False
                atualizar_mapa()
                checar_batalha()
        
        def Sul():
            limpar_curou()
            if est.y < y_len:
                est.y += 1
                est.afk = False
                atualizar_mapa()
                checar_batalha()
        
        def Oeste():
            limpar_curou()
            if est.x > 0:
                est.x -= 1
                est.afk = False
                atualizar_mapa()
                checar_batalha()

        def entrar():
            if mapa[est.y][est.x] == "loja":
               compra(game, atualizar_mapa)
            if mapa[est.y][est.x] == "prefeitura":
                prefeito()
            if mapa[est.y][est.x] == "caverna":
                est.boss = True
                caverna()

        perfil = f"""==================
LOCALIZAÇÃO X/Y: {bioma[mapa[est.y][est.x]]["t"]} - {est.x}/{est.y}
==================
{est.nome}
HP: {est.hp} / {est.max_hp}
ATK: {est.atk}
POÇÕES: {est.pocao}
ELIXIRES: {est.elixir}
NÍVEL: {est.nivel}
{est.xp} / {est.max_xp}
OURO: {est.ouro}
CRÍTICO: {est.crit}%
DANO_CRÍTICO: +{est.crit_dano}"""

        game = Tk()
        game.title("Jogo")
        game.attributes('-fullscreen', True)
        mapa_texto = gerar_mapa()
        mapa_label = Label(game, text=mapa_texto, anchor="w", justify="left", font=("Courier", 12))
        mapa_label.grid(row=0, column=0, sticky="w")
        mo_perfil = Label(game, text="", anchor="w", justify="left", font=("Courier", 12))
        mo_perfil.grid(row=1, column=0, sticky="w")
        mo_perfil["text"] = perfil
        ln_bt = 2
        if est.chave == "True":
            chave = Label(game, text="+1 CHAVE", anchor="w", justify="left", font=("Courier", 12)).grid(column=0, row=2, sticky="w")
            ln_bt += 1
        if est.fim == "True":
            es_dr = Label(game, text="ESCAMA DE DRAGÃO! (+20 ATK)", anchor="w", justify="left", font=("Courier", 12)).grid(column=0, row=3, sticky="w")
            ln_bt += 1
        curou = Label(game, text="", anchor="w", justify="left", font=("Courier", 12))
        curou.grid(column=0, row=ln_bt, sticky="w")
        Label(game, text="==================", anchor="w", justify="left", font=("Courier", 12)).grid(column=0, row=ln_bt+1, sticky="w")
        ln_bt += 2
        # Cria um Frame/Tabela para os botões
        larg_bt_game = 28
        botoes_frame = Frame(game)
        botoes_frame.grid(row=ln_bt, column=0, columnspan=1, sticky="n")
        game.grid_columnconfigure(0, weight=1)
        game.grid_rowconfigure(ln_bt, weight=1)
        for _ in range(3):
            botoes_frame.grid_columnconfigure(_, weight=0)
            botoes_frame.grid_rowconfigure(_, weight=0)
        Button(botoes_frame, text="USAR POÇÃO (+30 HP)", command=lambda: cura(1, curou, atualizar_mapa), width=larg_bt_game, font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5)
        Button(botoes_frame, text="NORTE (CIMA)", command=Norte, width=larg_bt_game, font=("Arial", 10)).grid(column=1, row=0, padx=5, pady=5)
        Button(botoes_frame, text="USAR ELIXIR (MAX_HP)", command=lambda: cura(2, curou, atualizar_mapa), width=larg_bt_game, font=("Arial", 10)).grid(column=2, row=0, padx=5, pady=5)
        Button(botoes_frame, text="OESTE (ESQUERDA)", command=Oeste, width=larg_bt_game, font=("Arial", 10)).grid(column=0, row=1, padx=5, pady=5)
        Button(botoes_frame, text="VOLTAR AO MENU", command=voltar, width=larg_bt_game, font=("Arial", 10)).grid(column=1, row=1, padx=5, pady=5)
        Button(botoes_frame, text="LESTE (DIREITA)", command=Leste, width=larg_bt_game, font=("Arial", 10)).grid(column=2, row=1, padx=5, pady=5)
        Button(botoes_frame, text="ENTRAR", command=entrar, width=larg_bt_game, font=("Arial", 10)).grid(column=0, row=2, padx=5, pady=5)
        Button(botoes_frame, text="SUL (BAIXO)", command=Sul, width=larg_bt_game, font=("Arial", 10)).grid(column=1, row=2, padx=5, pady=5)
        game.mainloop()
