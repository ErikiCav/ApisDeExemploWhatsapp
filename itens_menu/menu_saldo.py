from funcoes import Tarefas, InformacoesConta

def saldoEtapa0(numero, texto):
    Tarefas.atualizarEtapa(numero, 1)
    return "Informe sua senha para continuar!"

def saldoEtapa1(numero, texto):
    if(InformacoesConta.senhaValida(numero, texto)):
        nome = InformacoesConta.pegarNome(numero)
        Tarefas.atualizarComando(numero, "none")
        saldo = "{:,.2f}".format(float(InformacoesConta.pegarSaldo(numero))).replace(",","X").replace(".",",").replace("X",".")
        return f"""
*┌NOME.*
*├* {nome}.
*│*
*├SALDO.*
*└R$* {saldo}.       """
    else:
        Tarefas.atualizarComando(numero, "none")
        return "*Senha incorreta. Operação finalizada!*"