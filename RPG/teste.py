import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Frame Centralizado")

    # Cria o frame
    frame = tk.Frame(root, width=200, height=100, bg="lightblue")

    # Define o layout do frame usando grid()
    frame.grid(row=0, column=0, sticky="nsew")

    # Configura as linhas e colunas para centralização
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()