from tkinter import *
import estado as est
from save import save

def sair(m3nu):
    m3nu.withdraw()

    def sim():
        m3nu.destroy()
        sair_jogo.destroy()
        save(est.nome, est.hp, est.atk, est.pocao, est.elixir, est.ouro, est.x, est.y, est.chave, est.fim, est.xp, est.nivel, est.crit, est.crit_dano, est.max_hp, est.max_xp)
        quit()

    def nao():
        sair_jogo.destroy()
        m3nu.deiconify()
    
    sair_jogo = Tk()
    sair_jogo.title("Sair do Jogo")
    sair_jogo.attributes('-fullscreen', True)
    larg_bt_sair_jogo = 28
    Label(sair_jogo, text="Tem certeza que deseja sair?", font=("Courier", 12)).pack()
    Button(sair_jogo, text="Sim", command=lambda: sim(), width=larg_bt_sair_jogo, font=("Arial", 10)).pack()
    Button(sair_jogo, text="Não", command=lambda: nao(), width=larg_bt_sair_jogo, font=("Arial", 10)).pack()