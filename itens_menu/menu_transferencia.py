from funcoes import InformacoesConta, EtapasComandoTransferir, Tarefas
from utils.conveter_moeda import conveterMoeda

def transferenciaEtapa0(numero, texto):
    if(f"{texto}".replace(",","").replace(".","").isnumeric()):
        valor = conveterMoeda(texto)
        if(InformacoesConta.saldoSuficiente(numero, valor)):
            Tarefas.atualizarEtapa(numero, 1)
            EtapasComandoTransferir.atualizarValor(numero, valor)
            return "*OwO Você tem saldo o suficiente. Agora me informe o número de telefone do destinatário!*"
        else:
            return "*Desculpe, seu saldo é insuficiente, consulte seu saldo e tente novamente. Operação finalizada!*"
    else:
        Tarefas.atualizarComando(numero, "none")
        return "*Desculpe, apenas números, pontos e vírgulas são permitidos para essa entrada. Tente novamente!*"

def transferenciaEtapa1(numero, texto):
    destinatario = texto.replace("-","").replace(" ", "").replace("+55","")
    if(destinatario == numero):
        return "*Você não pode realizar transferências para sí próprio!*"
    else:
        if(InformacoesConta.checarExistencia(destinatario)):
            nome_destinatario = InformacoesConta.pegarNome(texto)
            EtapasComandoTransferir.atualizarDestino(numero, destinatario)
            valor_transferencia = EtapasComandoTransferir.pegarValor(numero)
            Tarefas.atualizarEtapa(numero, 2)
            return f"Owo, você está transferindo R$ *{valor_transferencia}* para *{nome_destinatario}*. Digite sua senha para continuar ou digite sair a qualquer momento!" 
        else:
            return "*Desculpe, este número de telefone não tem cadastro conosco. Tente novamente ou digite sair a qualquer momento!*"


def transferenciaEtapa2(numero, texto):
    if(InformacoesConta.senhaValida(numero, texto)):
        valor = conveterMoeda(EtapasComandoTransferir.pegarValor(numero))
        if(InformacoesConta.saldoSuficiente(numero, valor)):
            EtapasComandoTransferir.finalizarTransferencia(numero)
            Tarefas.atualizarComando(numero, "none")
            return f"*Transferência realizada com sucesso! :0*"
        else:
            Tarefas.atualizarComando(numero, "none")
            return "*Poxa. Estava aqui agora pouco :/ Infelizmente seu saldo é insuficiente. Operação finalizada!*"
    else:
        Tarefas.atualizarComando(numero, "none")
        return "*Senha incorreta. Operação finalizada!*"