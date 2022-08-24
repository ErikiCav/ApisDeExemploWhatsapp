from funcoes import EtapasComandoCriarConta, Tarefas

def criarContaEtapa0(numero):
    Tarefas.atualizarEtapa(numero, 1)
    return "Ok, vamos começar o seu cadastro. Como se chama? :)"

def criarContaEtapa1(numero, texto):
    EtapasComandoCriarConta.atualizarNome(numero, texto)
    Tarefas.atualizarEtapa(numero, 2)
    nome = EtapasComandoCriarConta.pegarNomeTemporario(numero)
    return f"Ok, *{nome}* . Agora me informe uma senha. Ela será usada para realizar transações, ok? :)"

def criarContaEtapa2(numero, texto):
    EtapasComandoCriarConta.atualizarSenha(numero, texto)
    Tarefas.atualizarEtapa(numero, 0)
    Tarefas.atualizarComando(numero, "none")
    EtapasComandoCriarConta.salvarConta(numero)
    EtapasComandoCriarConta.removerEtapaTemporaria(numero)
    return "Criei sua conta! Já pode fazer transferências. Parabéns, voce ganhou *R$ 400* que não poderá gastar! Aeeeee. :)"