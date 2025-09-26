from tkinter import *

def ajuda(m3nu):
    m3nu.withdraw()

    texto = """Guia do cavaleiro!
    1- Você começa na Floresta em 0/0.
    2- O Boss do jogo se localiza na Caverna.
    3- Para lutar contra o Boss você precisa de uma Chave.
    4- A Chave é obtida na Prefeitura com o Prefeito.
    5- Para pegar a Chave você precisa estar no Nível 20.
    6- Você consegue usar o botão de Entrar na Caverna, na Prefeitura e na Loja."""

    def voltar():
        guia.destroy()
        m3nu.deiconify()

    guia = Tk()
    guia.title("Ajuda")
    guia.attributes('-fullscreen', True)
    texto_ajuda = Label(guia, text="", font=("Courier", 12), anchor="w", justify="left", padx=10, pady=10)
    texto_ajuda["text"] = texto
    texto_ajuda.pack(anchor="w")
    larg_bt_ajuda = 28
    Button(guia, text="VOLTAR AO MENU", command=voltar, width=larg_bt_ajuda, font=("Arial", 10)).pack(anchor="center")
    guia.mainloop()
    