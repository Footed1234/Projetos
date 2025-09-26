import csv
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

produtos_totais = []

def verificar_csv():
    if not os.path.exists("banco.csv"):
        with open("banco.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["0"])


@app.route('/')
def home():
    verificar_csv()
    return render_template("BankIndex.html")


@app.route('/conta')
def conferir_conta():
    verificar_csv()
    with (open('banco.csv', mode='r') as file):
        conta = file.read()
        if conta == '':
            saldo_total = 0
        else:
            with (open('banco.csv', mode='r') as file):
                conta = csv.reader(file)
                saldo = list(conta)
                if saldo[0][0] == 0:
                    saldo_total = 0
                else:
                    saldo_total = float(saldo[0][0])

            with (open('banco.csv', mode='r') as file):
                conta = csv.reader(file)
                next(conta, None)
                linha = list(conta)
                if linha:
                    for itens in linha:
                        for item in itens:
                            if produtos_totais.count(item) < 1:    #conta quantos tem daquele item, se for 0 adiciona
                                item = str(item)
                                produtos_totais.append(item)

    return render_template('conta.html', saldo=saldo_total, produtos=produtos_totais)

@app.route('/deposit', methods=["GET", "POST"])
def deposit():
    verificar_csv()
    with (open('banco.csv', mode='r') as file):
        conta = csv.reader(file)
        saldo = list(conta)
        if saldo[0][0] == 0:
            saldo_total = 0
        else:
            saldo_total = float(saldo[0][0])

    if request.method == "POST":
        produto = request.form.get("produtos")
        saldo = request.form.get("saldo")

        if saldo:
            saldo_total += float(saldo)
        if produto:
            if produto not in produtos_totais:
                produtos_totais.append(produto)

        with open('banco.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([saldo_total])
            writer.writerows([produtos_totais])

        return redirect('/')
    return render_template('deposit.html')

@app.route('/retirar', methods=["GET", "POST"])
def retirar():
    with (open('banco.csv', mode='r') as file):
        conta = csv.reader(file)
        saldo = list(conta)
        if saldo[0][0] == 0:
            saldo_total = 0
        else:
            saldo_total = float(saldo[0][0])

    if request.method == "POST":
        produto = request.form.get("produtos")
        saldo = request.form.get("saldo")

        if saldo:
            if float(saldo) <= saldo_total:
                saldo_total -= float(saldo)
        if produto:
            if produto in produtos_totais:
                produtos_totais.remove(produto)

        with open('banco.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([saldo_total])
            writer.writerows([produtos_totais])

        return redirect('/')
    return render_template('retirar.html', saldo=saldo_total, produtos=produtos_totais)

app.run()