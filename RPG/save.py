def save(nome, hp, atk, pocao, elixir, ouro, x, y, chave, fim, xp, nivel, crit, crit_dano, max_hp, max_xp):
    dados = [nome, str(hp), str(atk), str(pocao), str(elixir), str(ouro), str(x), str(y), chave, fim, str(xp), str(nivel), str(crit), str(crit_dano), str(max_hp), str(max_xp)]

    file = open("save.txt", "w")
    for item in dados:
        file.write(f"{item}\n")
    file.close()

def get_save():
    try:
        file = open("save.txt", "r")
        lista = file.readlines()
        if len(lista) == 16:  # save
            nome = lista[0][:-1]  # :-1, tira o último dígito, no caso, o espaço
            hp = int(lista[1][:-1])
            atk = int(lista[2][:-1])
            pocao = int(lista[3][:-1])
            elixir = int(lista[4][:-1])
            ouro = int(lista[5][:-1])
            x = int(lista[6][:-1])
            y = int(lista[7][:-1])
            chave = lista[8][:-1]
            fim = lista[9][:-1]
            xp = int(lista[10][:-1])
            nivel = int(lista[11][:-1])
            crit = int(lista[12][:-1])
            crit_dano = float(lista[13][:-1])
            max_hp = int(lista[14][:-1])
            max_xp = int(lista[15][:-1])
            return nome, hp, atk, pocao, elixir, ouro, x, y, chave, fim, xp, nivel, crit, crit_dano, max_hp, max_xp
        else:
            print("Arquivo corrompido")
            print("Pressione qualquer botão para voltar ao menu")
    except OSError:
                print("Nenhum arquivo existente")
                print("Pressione qualquer botão para voltar ao menu")
    input()