from flask import Flask, request
from funcoes import criarPadrao
from controle import controle, controleOutrasApis

app = Flask(__name__)


@app.route('/PrivateApis')
def privateApis():
    numero = request.args["numero"].replace(" ","").replace("-","")
    texto = request.args["texto"]
    return controleOutrasApis(numero, texto)

@app.route('/ApiWpp')
def apiWpp():
    numero = request.args["numero"].replace(" ","").replace("-","")
    texto = request.args["texto"]
    return controle(numero, texto)

criarPadrao()
if __name__ == '__main__':
    app.run("0.0.0.0", 5000 )