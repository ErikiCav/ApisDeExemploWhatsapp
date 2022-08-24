from funcoes import Tarefas
from itens_menu.menu_criar_conta import criarContaEtapa0, criarContaEtapa1, criarContaEtapa2
from itens_menu.menu_saldo import saldoEtapa0, saldoEtapa1
from itens_menu.menu_transferencia import transferenciaEtapa0, transferenciaEtapa1, transferenciaEtapa2
from itens_menu.menu_menu import menuEtapa0

#Controle de etapas de criar conta.
def criarConta(numero, texto):
    if(Tarefas.pegarComando(numero) == "cadastrar"):
        if((int(Tarefas.pegarEtapa(numero))) == 0):
            return criarContaEtapa0(numero)

        if((int(Tarefas.pegarEtapa(numero))) == 1):
            return criarContaEtapa1(numero, texto)

        if((int(Tarefas.pegarEtapa(numero))) == 2):
            return criarContaEtapa2(numero, texto)

#Controle de etapas menu.
def menu(numero, texto):
    if(Tarefas.pegarComando(numero) == "menu"):
        if((int(Tarefas.pegarEtapa(numero))) == 0):
            return menuEtapa0(numero, texto)

#Controle de etapas de transferencia.
def transferencia(numero, texto):
    if(Tarefas.pegarComando(numero) == "transferir"):
        if((int(Tarefas.pegarEtapa(numero))) == 0):
            return transferenciaEtapa0(numero, texto)

        if((int(Tarefas.pegarEtapa(numero))) == 1):
            return transferenciaEtapa1(numero, texto)

        if((int(Tarefas.pegarEtapa(numero))) == 2):
            return transferenciaEtapa2(numero, texto)

#Controle de etapas consulta de saldo.
def consultarSaldo(numero, texto):
    if(Tarefas.pegarComando(numero) == "consultarSaldo"):
        if((int(Tarefas.pegarEtapa(numero))) == 0):
            return saldoEtapa0(numero, texto)

        if((int(Tarefas.pegarEtapa(numero))) == 1):
            return saldoEtapa1(numero, texto)