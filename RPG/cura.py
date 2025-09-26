import estado as est
from tkinter import *

def cura(tipo, pl_stat, atualizar_mapa):
    if est.pocao > 0 or est.elixir > 0:
        if tipo == 1:
            if est.pocao > 0:
                est.pocao -= 1
                if est.hp + 30 < est.max_hp:
                    est.hp += 30
                else:
                    est.hp = est.max_hp
        else:
            if est.elixir > 0:
                est.elixir -= 1
                est.hp = est.max_hp
        pl_stat.config(text=f"{est.nome} curou e está com {est.hp} de HP!")
        atualizar_mapa()
        pl_stat.after(2500, lambda: pl_stat.config(text=""))
    atualizar_mapa()