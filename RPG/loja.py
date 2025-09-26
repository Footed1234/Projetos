import estado as est
from tkinter import *

def compra(game, atualizar_mapa):
    game.withdraw()

    def atualizar_loja():
        ouro_lbl.config(text=f"OURO: {est.ouro}")
        pocao_lbl.config(text=f"POÇÕES: {est.pocao}")
        elixir_lbl.config(text=f"ELIXIRES: {est.elixir}")

    def erro_loja():
        erro_lbl.config(text="Você não tem ouro suficiente!")
        erro_lbl.after(2500, lambda: erro_lbl.config(text=""))        

    def comprou_lbl(item, custo):
        comprou = f"""+1 {item}!
-{custo} ouro!"""
        compra.config(text=comprou)
        compra.after(2500, lambda: compra.config(text=""))

    def comprar_pocao():
        if est.ouro >= 20:
            est.pocao += 1
            est.ouro -= 20
            atualizar_loja()
            comprou_lbl("poção", 20)
        else:
            erro_loja()
        
    def comprar_elixir():
        if est.ouro >= 80:
            est.elixir += 1
            est.ouro -= 80
            atualizar_loja()
            comprou_lbl("elixir", 80)
        else:
            erro_loja()

    def sair_loja():
        game.deiconify()
        loja.destroy()
        atualizar_mapa()

    loja = Tk()
    loja.title("Loja")
    loja.attributes('-fullscreen', True)
    Label(loja, text="Bem-Vindo(a) à Loja!", anchor="w", justify="left", font=("Courier", 12)).grid(sticky="w", row=0)
    Label(loja, text="==================", anchor="w", justify="left",  font=("Courier", 12)).grid(sticky="w", row=1)
    Label(loja, text="Seu inventário:", anchor="w", justify="left", font=("Courier", 12)).grid(sticky="w", row=2)
    ouro_lbl = Label(loja, text=f"OURO: {est.ouro}", anchor="w", justify="left", font=("Courier", 12))
    ouro_lbl.grid(sticky="w", row=3)
    pocao_lbl = Label(loja, text=f"POÇÕES: {est.pocao}", anchor="w", justify="left", font=("Courier", 12))
    pocao_lbl.grid(sticky="w", row=4)
    elixir_lbl = Label(loja, text=f"ELIXIRES: {est.elixir}", anchor="w", justify="left", font=("Courier", 12))
    elixir_lbl.grid(sticky="w", row=5)
    Label(loja, text="==================", anchor="w", justify="left", font=("Courier", 12)).grid(sticky="w", row=6)
    Label(loja, text="Tabela de preços", anchor="w", justify="left", font=("Courier", 12)).grid(sticky="w", row=7)
    Label(loja, text="Poção -> 20 ouro", anchor="w", justify="left", font=("Courier", 12)).grid(sticky="w", row=8)
    Label(loja, text="Elixir -> 80 ouro", anchor="w", justify="left", font=("Courier", 12)).grid(sticky="w", row=9)
    Label(loja, text="==================", anchor="w", justify="left", font=("Courier", 12)).grid(sticky="w", row=10)
    compra = Label(loja, text="", anchor="w", justify="left", font=("Courier", 12))
    compra.grid(sticky="w", row=11)
    erro_lbl = Label(loja, text="", anchor="w", justify="left", font=("Courier", 12), fg="red")
    erro_lbl.grid(sticky="w", row=12)
    # Cria um Frame/Tabela para os botões
    larg_bt_loja = 28
    botoes_frame = Frame(loja)
    botoes_frame.grid(row=13, column=0, columnspan=1, sticky="n")
    loja.grid_columnconfigure(0, weight=1)
    loja.grid_rowconfigure(13, weight=1)
    for _ in range(2):
        botoes_frame.grid_columnconfigure(_, weight=0)
        botoes_frame.grid_rowconfigure(_, weight=0)
    Button(botoes_frame, text="Comprar Poção (+30 HP) -> 20 ouro", command=lambda: comprar_pocao(), width=larg_bt_loja).grid(column=0, row=0, padx=5, pady=5)
    Button(botoes_frame, text="Comprar Elixir (MAX_HP) -> 80 ouro", command=lambda: comprar_elixir(), width=larg_bt_loja).grid(column=1, row=0, padx=5, pady=5)
    Button(botoes_frame, text="Sair", command=lambda: sair_loja(), width=larg_bt_loja).grid(column=1, row=1, padx=5, pady=5)
    loja.mainloop()