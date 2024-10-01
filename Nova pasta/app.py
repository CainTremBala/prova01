from flask import Flask, render_template
from lanche import Lanche

app = Flask(__name__)

lanche_list = [
    Lanche(1, 'Coxinha', 6.00, 'Essa é uma coxinha caríssima!', 'coxinha.png'),
    Lanche(2, 'Coca-Cola', 8.00, 'Isso é uma Coca-Cola gelada!', 'coca.png'),
    Lanche(3, 'Kibe', 10.00, 'Isso é um Kibe de Itú!', 'kibe.png'),
    Lanche(4, 'Empada', 7.00, 'Empada da Broadway cara pra caramba', 'empada.png'),
    Lanche(5, 'Pastel', 3.00, 'Pastel de casa porque tô sem grana', 'pastel.png'),
]

@app.route("/")
def home():
    return render_template("index.html", lanche_list=lanche_list)

@app.route("/lanche/<int:id>")
def lanche(id):
    for lanche in lanche_list:
        if lanche.get_id() == id:
            return render_template("lanches.html", lanche=lanche)
    return '<h1>Ops! Nenhum lanche encontrado!</h1>'