from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome  = nome
        self.categoria = categoria
        self.console = console
    def setNome(self, nome):
        self.nome = nome
    def setCategoria(self, categoria):
        self.categoria = categoria
    def setConsole(self, console):
        self.console = console
    def getNome(self):
        return self.nome
    def getCategoria(self):
        return self.categoria
    def getConsole(self):
        return self.console
list = []
list.append(Jogo('Tetris', 'Puzzle', 'Atari'))
list.append(Jogo('God of War', 'Hack n Slash', 'PS2'))
for obj in list:
    print(obj.nome, obj.categoria, obj.console, sep='')

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Meus Jogos', jogos=list)

app.run()