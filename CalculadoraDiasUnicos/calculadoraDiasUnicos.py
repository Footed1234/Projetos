from datetime import date, timedelta

def tem_digitos_unicos(data):
    # pega a data no formato DDMMYYYY -> 21102025
    digitos = data.strftime("%d%m%Y")
    # set() remove números duplicados
    # se o tamanho da string depois do set() for 8, todos os dígitos são únicos
    return len(set(digitos)) == 8

print("Calculadora de Dias com Dígitos Únicos")
print("=====================================")
print("Pressione qualquer botão para continuar...")
input("> ")
inicio = int(input("Digite o ano de início (ex: 1900): "))
fim = int(input("Digite o ano de fim (ex: 1999): "))

# seta as datas de início e fim
inicio = date(inicio, 1, 1)
fim = date(fim, 12, 31)

# variável que guarda quantos são os dias com dígitos únicos
contador = 0

while inicio <= fim:
    # se todos os dígitos forem únicos, incrementa o contador
    if tem_digitos_unicos(inicio):
        contador += 1
    # avança para o próximo dia -> 22102025
    inicio += timedelta(days=1)

# print final do resultado
print("Total de datas com dígitos únicos:", contador)