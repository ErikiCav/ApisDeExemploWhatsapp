import requests
from funcoes import InformacoesConta, Tarefas
from controles.controles import criarConta, menu, transferencia, consultarSaldo

def controle(numero, texto):
    if(f"{texto}".lower() == "consultar saldo") | (f"{texto}".lower() == "2"):
        if not(InformacoesConta.checarExistencia(numero)):
            return "Olá, identifiquei que *você não possui uma conta criada* ! :/ Digite cadastrar para criar uma!"
        else:
            Tarefas.atualizarComando(numero, "consultarSaldo")
            Tarefas.atualizarEtapa(numero, 0)
            return consultarSaldo(numero, texto)

    if("sair" == f"{texto}".lower()):
        if not(InformacoesConta.checarExistencia(numero)):
            return "Olá, identifiquei que *você não possui uma conta criada* ! :/ Digite cadastrar para criar uma!"
        else:
            Tarefas.atualizarEtapa(numero, 0)
            Tarefas.atualizarComando(numero, "none")
            return "Operações finalizadas!"

    if("cadastrar" == f"{texto}".lower()):
        if(InformacoesConta.checarExistencia(numero)):
            nome = InformacoesConta.pegarNome(numero)
            return f"Desculpe *{nome}*. Você já possui uma conta criada. Digite *menu* para listar as opções disponíveis para você! :)"
        else:
            Tarefas.criarTarefa(numero)
            Tarefas.atualizarComando(numero, "cadastrar")
            Tarefas.atualizarEtapa(numero, 0)
            return criarConta(numero, texto)

    if("menu" in f"{texto}".lower()):
        if not(InformacoesConta.checarExistencia(numero)):
            return "Olá, identifiquei que *você não possui uma conta criada* ! :/ Digite cadastrar para criar uma!"
        else:
            Tarefas.atualizarComando(numero, "menu")
            Tarefas.atualizarEtapa(numero, 0)
            return "Informe sua senha para continuar!"
    
    if((f"{texto}".lower() == "transferir") | (f"{texto}".lower() == "1")):
        Tarefas.atualizar_comando(numero, "none")
        if not(InformacoesConta.checarExistencia(numero)):
            return "Olá, identifiquei que *você não possui uma conta criada* ! :/ Digite cadastrar para criar uma!"
        else:
            Tarefas.atualizarComando(numero, "transferir")
            Tarefas.atualizarEtapa(numero, 0)
            return "Informe o valor de sua transferência!"

    else:
        comando = Tarefas.pegarComando(numero)
        if not(comando == "none"):
            if(comando == "cadastrar"):
                return criarConta(numero, texto)

            if(comando == "menu"):
                return menu(numero,texto)
            
            if(comando == "transferir"):
                return transferencia(numero, texto)
            
            if(comando == "consultarSaldo"):
                return consultarSaldo(numero, texto)


    #Se o texto recebido não for pego pelos retornos acima, retorne uma String padrão que vai ser usada para que o aplicativo ignore a mensagem.
    #Isto e a definição de comandos faz com que a API economize, já que não vai mandar todos os textos enviados ao bot para uma requesição ao banco de dados e à outras funções mais pesadas, a menos que queira.
    return "sem_retorno_x01Bt4TY2d"


def controleOutrasApis(numero, texto):
    if("/python3" in f"{texto}".lower()):
        if(f"{texto}".lower() == "/python3"):
            return "Esqueceu-se de informar o *código em python3* que deseja que eu execute, junto ao comando!"
        else:
            return "*Saída:*\n\n"+requests.get(f"https://erikicav-privateapis.herokuapp.com/python3run?codigo="+texto.split(" ",1)[1]).text

    return "🤖: "+"*"+requests.get(f"https://erikicav-privateapis.herokuapp.com/ed_InteligenciaArtificial.py?texto="+texto+"&&user_id="+numero[2:3]+"1Ytfq55w1!3ssw"+numero[6:9]).text+"*"
