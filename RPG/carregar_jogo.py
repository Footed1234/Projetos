from tkinter import *
from save import get_save
import estado as est

def carregar_jogo(m3nu):
    m3nu.withdraw() 

    def carregar2():
        est.nome, est.hp, est.atk, est.pocao, est.elixir, est.ouro, est.x, est.y, est.chave, est.fim, est.xp, est.nivel, est.crit, est.crit_dano, est.max_hp, est.max_xp = get_save()
        welcome_label.config(text=f"Bem-vindo(a) {est.nome}")
        ca_jo.after(2000, ca_iniciar_jogo)

    def voltar():
        ca_jo.destroy()
        m3nu.deiconify()

    def ca_iniciar_jogo():
            ca_jo.destroy()
            m3nu.destroy()
            est.menu = False
            est.jogar = True

    # Janela de carregar o jogo
    ca_jo = Tk()
    ca_jo.title("Carregar Jogo")
    ca_jo.attributes('-fullscreen', True)
    larg_bt_ca_jo = 28
    Label(ca_jo, text="Carregar jogo?", font=("Courier", 12)).pack()
    Button(ca_jo, text="Sim", command=carregar2, font=("Arial", 10), width=larg_bt_ca_jo).pack()
    Button(ca_jo, text="Não", command=voltar, font=("Arial", 10), width=larg_bt_ca_jo).pack()
    welcome_label = Label(ca_jo, text="", font=("Courier", 12))
    welcome_label.pack()
    ca_jo.mainloop()