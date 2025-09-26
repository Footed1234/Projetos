from tkinter import *
import estado as est

def novo_jogo(m3nu):
    m3nu.withdraw()
    
    def voltar():
        no_jo.destroy()
        m3nu.deiconify()
    
    def escrever_nome():
        no_jo.destroy()
        def salvar_nome():
            est.nome = nome_pl.get()
            if est.nome == "":
                erro_label.config(text="Nome inválido! Campo Obrigatório!")
                return
            else:
                welcome_label.config(text=f"Bem-vindo(a) {est.nome}")
                es_no.after(2000, no_iniciar_jogo)
        
        def no_iniciar_jogo():
            es_no.destroy()
            m3nu.destroy()
            est.menu = False
            est.jogar = True

        # Janela para escrever o nome
        es_no = Tk()
        es_no.title("Nome")
        es_no.attributes('-fullscreen', True)
        larg_bt_es_no = 28
        # Digite seu nome
        Label(es_no, text="Digite seu nome", font=("Courier", 12)).pack()
        # Espaço para digitar o nome
        nome_pl = Entry(es_no, width=larg_bt_es_no, font=("Arial", 10))
        nome_pl.pack()
        # Quando o nome for digitado incorretamente
        erro_label = Label(es_no, text="", fg="red", font=("Courier", 12))
        erro_label.pack()
        # Botão para salvar o nome
        Button(es_no, text="Salvar", command=salvar_nome, width=larg_bt_es_no, font=("Arial", 10)).pack()
        # Quando digitar o nome corretamente
        welcome_label = Label(es_no, text="", font=("Courier", 12))
        welcome_label.pack()
        es_no.mainloop()
        
    # Janela de novo jogo
    no_jo = Tk()
    no_jo.title("Novo Jogo?")
    no_jo.attributes('-fullscreen', True)
    larg_bt_no_jo = 28
    Label(no_jo, text="Novo jogo?", font=("Courier", 12)).pack()
    Button(no_jo, text="Sim", command=escrever_nome, width=larg_bt_no_jo, font=("Arial", 10)).pack()
    Button(no_jo, text="Não", command=voltar, width=larg_bt_no_jo, font=("Arial", 10)).pack()
    no_jo.mainloop()