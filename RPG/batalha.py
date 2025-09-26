import random, os
from tkinter import *
import estado as est
from niveis import up_nivel
from mobs import mobs
from cura import cura
from novo_jogo import novo_jogo
from carregar_jogo import carregar_jogo
from ajuda import ajuda
from sair_jogo import sair

lista_inimigos = ["Goblin", "Ogro", "Slime"]

def x_inimigo():
    inimigo = random.choice(lista_inimigos)
    return inimigo

global inimigo, i_atk, i_hp, i_max_hp, i_ouro, i_xp

def batalha(game, atualizar_mapa, curou):
    est.luta = True
    game.withdraw()

    if not est.boss:
        inimigo = x_inimigo()
    else:
        inimigo = "Dragão"
    i_hp = mobs[inimigo]["i_hp"]
    i_max_hp = i_hp
    i_atk = mobs[inimigo]["i_atk"]
    i_ouro = mobs[inimigo]["i_ouro"]
    i_xp = mobs[inimigo]["i_xp"]


    fight = Tk()
    fight.title("Batalha")
    fight.attributes('-fullscreen', True)
    mo_x1 = Label(fight, text="", font=("Courier", 12), anchor="w", justify="left")
    mo_x1.grid(column=0, row=0, sticky="w")
    
    def atualizar_x1():
        novo_x1 = f"""Derrote {inimigo}!
==================
Vida de {inimigo}: {i_hp} / {i_max_hp}
Vida de {est.nome}: {est.hp} / {est.max_hp}
POÇÕES: {est.pocao}
ELIXIR: {est.elixir}
=================="""
        mo_x1.config(text=novo_x1)

    def curar_pl(tipo):
        if tipo == 1:
            cura(1, pl_stat, atualizar_mapa)
        if tipo == 2:
            cura(2, pl_stat, atualizar_mapa)
        fight.after(2500, atk_inimigo)

    def abrir_menu():
            # Janela do menu
            m3nu = Tk()
            m3nu.title("Menu do Jogo")
            m3nu.attributes('-fullscreen', True)
            Button(m3nu, text="Novo Jogo", command=lambda: novo_jogo(m3nu)).pack()
            Button(m3nu, text="Carregar Jogo", command=lambda: carregar_jogo(m3nu)).pack()
            Button(m3nu, text="Ajuda", command=lambda: ajuda(m3nu)).pack()
            Button(m3nu, text="Sair do Jogo", command=lambda: sair(m3nu)).pack()
            m3nu.mainloop()

    def recompensa(vencedor, recompensas):
        recompensa_win = Toplevel(game)
        recompensa_win.title("Recompensas")
        recompensa_win.attributes('-fullscreen', True)
        ven = Label(recompensa_win, text="", font=("Courier", 12), anchor="w", justify="left")
        ven.pack(anchor="w")
        Label(recompensa_win, text="==================", anchor="w", justify="left", font=("Courier", 12)).pack(anchor="w")
        if vencedor == "player":
            est.xp, est.nivel, est.atk, est.max_hp, est.max_xp, est.crit, est.crit_dano = up_nivel(est.xp, est.nivel, est.atk, est.max_hp, est.max_xp, est.crit, est.crit_dano, i_xp)
            ven.config(text=f"{est.nome} derrotou {inimigo}!")
            Label(recompensa_win, text=recompensas, font=("Courier", 12), anchor="w", justify="left").pack(anchor="w")
            Label(recompensa_win, text="==================", anchor="w", justify="left", font=("Courier", 12)).pack(anchor="w")
            Button(recompensa_win, text="Continuar", command=lambda: (game.deiconify(), recompensa_win.destroy(), atualizar_mapa())).pack(anchor="w")
        else:
            ven.config(text=f"{inimigo} derrotou {est.nome}!")
            Label(recompensa_win, text="Você foi derrotado!", font=("Courier", 12), anchor="w", justify="left").pack(anchor="w")
            Label(recompensa_win, text="==================", anchor="w", justify="left", font=("Courier", 12)).pack(anchor="w")
            Button(recompensa_win, text="Voltar ao Menu", command=lambda: (recompensa_win.destroy(), game.destroy(), abrir_menu())).pack(anchor="w")

    def atk_player():
        nonlocal i_hp
        dano = 0
        if random.randint(0, 100) <= 80:  #  80% chance de acertar o ataque
            if random.randint(0, 100) <= 30:  # 30% chance do inimigo defender
                pl_stat.config(text=f"{inimigo} defendeu o ataque de {est.nome}!")
            else:
                if random.randint(0, 100) <= est.crit:  # player_crit% chance de crítico
                    pl_stat.config(text=f"CRÍTICO! {est.nome} deu {est.atk + est.crit_dano} de dano em {inimigo}!")
                    dano = est.atk + est.crit_dano
                else:
                    pl_stat.config(text=f"{est.nome} deu {est.atk} de dano em {inimigo}!")
                    dano = est.atk
        else:
            pl_stat.config(text=f"{est.nome} errou o ataque!")
        pl_stat.after(1500, lambda: pl_stat.config(text=""))
        i_hp -= dano
        atualizar_x1()
        pocao = False
        elixir = False
        if i_hp <= 0:
            if random.randint(0, 100) <= 60:
                est.pocao += 1
                pocao = True
            if random.randint(0, 100) <= 30:
                est.elixir += 1
                elixir = True
            est.ouro += i_ouro
            fight.after(500, lambda: (recompensa(vencedor="player", recompensas=
                    f"+{i_ouro} OURO\n+{i_xp} XP\n" +
                    (f"+1 POÇÃO\n" if pocao == True else "") +
                    (f"+1 ELIXIR\n" if elixir == True else "") +
                    ("Parabéns! Você derrotou o Dragão e zerou o jogo!\n" if inimigo == "Dragão" else "")),
                    fight.destroy()))
        else:
            fight.after(1500, atk_inimigo)
    
    def atk_inimigo():
        dano = 0
        if random.randint(0, 100) <= 80:  # 80% chance de acertar o ataque
            if random.randint(0, 100) <= 50:  # 50% chance do player defender
                in_stat.config(text=f"{est.nome} defendeu o ataque de {inimigo}!")
            else:
                if random.randint(0, 100) <= 30:  # 30% chance de crítico
                    in_stat.config(text=f"CRÍTICO! {inimigo} deu {i_atk + 2} de dano em {est.nome}!")
                    dano = i_atk + 2
                else:
                    in_stat.config(text=f"{inimigo} deu {i_atk} de dano em {est.nome}!")
                    dano = i_atk
        else:
            in_stat.config(text=f"{inimigo} errou o ataque!")
        in_stat.after(1500, lambda: in_stat.config(text=""))
        est.hp -= dano
        atualizar_x1()
        if est.hp <= 0: 
            fight.after(500, lambda: ( 
                recompensa("inimigo",""), fight.destroy()))

    def limpar_curou():
            curou.config(text="")

    atualizar_x1()
    pl_stat = Label(fight, text="", font=("Courier", 12), anchor="w", justify="left")
    pl_stat.grid(column=0, row=1, sticky="w")
    in_stat = Label(fight, text="", font=("Courier", 12), anchor="w", justify="left")
    in_stat.grid(column=0, row=2, sticky="w")
    Label(fight, text="==================", anchor="w", justify="left", font=("Courier", 12)).grid(column=0, row=3, sticky="w")
    # Cria um Frame/Tabela para os botões
    larg_bt_bat = 28
    botoes_frame = Frame(fight)
    botoes_frame.grid(row=4, column=0, columnspan=1, sticky="n")
    for _ in range(2):
        botoes_frame.grid_columnconfigure(_, weight=0)
        botoes_frame.grid_rowconfigure(_, weight=0)
    fight.grid_rowconfigure(4, weight=1)
    fight.grid_columnconfigure(0, weight=1)
    Button(botoes_frame, text="ATACAR", command=lambda: (atk_player(), limpar_curou()), width=larg_bt_bat, font=("Arial", 10)).grid(column=0, row=0, padx=5, pady=5)
    Button(botoes_frame, text="USAR POÇÃO (+30 HP)", command=lambda: curar_pl(1), width=larg_bt_bat, font=("Arial", 10)).grid(column=0, row=1, padx=5, pady=5)
    Button(botoes_frame, text="USAR ELIXIR (MAX_HP)", command=lambda: curar_pl(2), width=larg_bt_bat, font=("Arial", 10)).grid(column=1, row=1, padx=5, pady=5)
    Button(botoes_frame, text="FUGIR", command=lambda: (fight.destroy(), game.deiconify(), atualizar_mapa()), width=larg_bt_bat, font=("Arial", 10)).grid(column=1, row=0, padx=5, pady=5)
    fight.mainloop()


    # if est.hp <= 0:
    #     print(f"{inimigo} derrotou {est.nome}...")
    #     desenho()
    #     est.luta = False
    #     print("Fim de Jogo!")
    #     print("Você pode voltar para o último save!")
    #     input()
    #     quit()
    # if i_hp <= 0:
    #     print(f"{est.nome} derrotou {inimigo}!")
    #     pre_nivel = est.nivel
    #     pre_crit = est.crit
    #     pre_crit_dano = est.crit_dano
    #     desenho()
    #     est.luta = False
    #     est.ouro += i_ouro
    #     est.xp, est.nivel, est.atk, est.max_hp, est.max_xp, est.crit, est.crit_dano = up_nivel(est.xp, est.nivel, est.atk, est.max_hp, est.max_xp, est.crit, est.crit_dano, inimigo)
    #     print(f"+{i_ouro} OURO!")
    #     print(f"+{i_xp} XP!")
    #     if est.nivel - pre_nivel > 0:
    #         print(f"+{est.nivel - pre_nivel} NÍVEL(IS)!")
    #         if est.crit - pre_crit > 0:
    #             print(f"+{est.crit - pre_crit}% DE CRÍTICO!")
    #         print(f"+{est.crit_dano - pre_crit_dano} DANO CRÍTICO!")
    #     if random.randint(0, 100) <= 60:
    #         est.pocao += 1
    #         print("+1 POÇÃO!")
    #     if random.randint(0, 100) <= 30:
    #         est.elixir += 1
    #         print("+1 ELIXIR!")
    #     if inimigo == "Dragão":
    #         desenho()
    #         print("Parabéns! Você derrotou o Dragão e zerou o jogo!")
    #         est.fim = "True"
    #         est.atk += 20
    #         est.boss = False
    #     input()
    #     return est.hp, est.pocao, est.elixir, est.atk, est.boss, est.fim, est.xp, est.nivel, est.max_hp, est.max_xp, est.crit, est.crit_dano
            