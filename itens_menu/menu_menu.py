from datetime import datetime
from funcoes import Tarefas, InformacoesConta
from utils.get_day import getDay

def menuEtapa0(numero, texto):
    if(InformacoesConta.senhaValida(numero, texto)):
        nome = InformacoesConta.pegarNome(numero)
        Tarefas.atualizarComando(numero, "none")
        return f"""{getDay(datetime.today().strftime("%H%M"))}, *{nome}*. Escolha uma das opções, basta me enviar o número da opção ou me falar o que deseja!QUEBRALINHAQUEBRALINHA*1-* Transferir.QUEBRALINHA*2-* Consultar saldo."""
    else:
        Tarefas.atualizarComando(numero, "none")
        return "*Senha incorreta. Operação finalizada!*"