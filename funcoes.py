import sqlite3

#Aqui inicia todo o gerenciamento de banco de dados.
def conectar():
    return sqlite3.connect("dados.db")

def criarPadrao():
    db = conectar()
    db.executescript("PRAGMA jounal_mode=WAL")
    db.executescript("CREATE TABLE IF NOT EXISTS CONTAS(NUMERO TEXT PRIMARY KEY NOT NULL, SALDO TEXT KEY NOT NULL, NOME TEXT NOT NULL, SENHA TEXT NOT NULL);")
    
    db.executescript("CREATE TABLE IF NOT EXISTS TAREFAS(ETAPA TEXT NOT NULL, COMANDO TEXT NOT NULL, NUMERO PRIMARY KEY NOT NULL);")
    
    db.executescript("CREATE TABLE IF NOT EXISTS CRIAR_CONTA(NUMERO TEXT PRIMARY KEY NOT NULL, SENHA TEXT NOT NULL, NOME TEXT NOT NULL);")

    db.executescript("CREATE TABLE IF NOT EXISTS TRANSFERENCIA(NUMERO TEXT PRIMARY KEY NOT NULL, VALOR TEXT NOT NULL, DESTINO TEXT not NULL);")
    
    db.commit()
    db.close()

#Gerencia tarefas
class Tarefas:
    def criarTarefa(numero):
        try:
            db = conectar()
            db.executescript(f"""INSERT INTO TAREFAS(ETAPA, COMANDO, NUMERO) VALUES ('0','none','{numero}')""")
            db.executescript(f"INSERT INTO CRIAR_CONTA(NUMERO, NOME, SENHA) VALUES ('{numero}', 'none','none');")
            db.executescript(f"INSERT INTO TRANSFERENCIA(NUMERO, VALOR, DESTINO) VALUES ('{numero}', 'none','none');")
            db.commit()
            db.close()
        except:
            pass

    def atualizarComando(numero, comando):
        db = conectar()
        db.executescript(f"UPDATE TAREFAS SET COMANDO='{comando}' WHERE NUMERO='{numero}'")
        db.commit()
        db.close()

    def atualizarEtapa(numero, etapa):
        db = conectar()
        db.executescript(f"UPDATE TAREFAS SET ETAPA='{etapa}' WHERE NUMERO='{numero}'")
        db.commit()
        db.close()

    def pegarEtapa(numero):
        db = conectar()
        D = db.execute(f"SELECT ETAPA FROM TAREFAS WHERE NUMERO='{numero}'").fetchone()[0]
        db.commit()
        db.close()
        return D

    def pegarComando(numero):
        db = conectar()
        try:
            D = db.execute(f"SELECT COMANDO FROM TAREFAS WHERE NUMERO='{numero}'").fetchone()[0]
            db.commit()
            db.close()
            return D
        except:
            db.close()
        return "none"
    
#Gerencia etapas do comando de cadastro de contas.
class EtapasComandoCriarConta:

    def atualizarNome(numero, nome):
        db = conectar()
        db.executescript(f"UPDATE CRIAR_CONTA SET NOME='{nome}' WHERE NUMERO='{numero}'")
        db.commit()
        db.close()

    def pegarNomeTemporario(numero):
        db = conectar()
        D = db.execute(f"SELECT NOME FROM CRIAR_CONTA WHERE NUMERO='{numero}'").fetchone()[0]
        db.commit()
        db.close()
        return D

    def atualizarSaldo(numero, saldo):
        db = conectar()
        db.executescript(f"UPDATE CRIAR_CONTA SET SALDO='{saldo}' WHERE NUMERO='{numero}'")
        db.commit()
        db.close()
    
    def atualizarSenha(numero, senha):
        db = conectar()
        db.executescript(f"UPDATE CRIAR_CONTA SET SENHA='{senha}' WHERE NUMERO='{numero}'")
        db.commit()
        db.close()
    
    def salvarConta(numero):
        db = conectar()
        conta = db.execute(f"SELECT * FROM CRIAR_CONTA WHERE NUMERO='{numero}'").fetchone()
        senha = conta[1]
        nome = conta[2]
        db.executescript(f"INSERT INTO CONTAS(numero, saldo, nome, senha) VALUES ('{numero}', '400.00','{nome}','{senha}')")
        db.commit()
        db.close()
    
    def removerEtapaTemporaria(numero):
        db = conectar()
        db.executescript(f"DELETE FROM CRIAR_CONTA WHERE NUMERO='{numero}'")
        db.commit()
        db.close()

#Gerencia etapas do comando de transferencia.
class EtapasComandoTransferir:

    def atualizarDestino(numero, destino):
        db = conectar()
        db.executescript(f"UPDATE TRANSFERENCIA SET DESTINO='{destino}' WHERE NUMERO='{numero}'")
        db.commit()
        db.close()
    
    def atualizarValor(numero, valor):
        db = conectar()
        db.executescript(f"UPDATE TRANSFERENCIA SET VALOR='{valor}' WHERE NUMERO='{numero}'")
        db.commit()
        db.close()

    def pegarValor(numero):
        db = conectar()
        D = db.execute(f"SELECT VALOR FROM TRANSFERENCIA WHERE NUMERO='{numero}'").fetchone()[0]
        db.commit()
        db.close()
        return D
    
    def pegarDadosTransferencia(numero):
        db = conectar()
        D = db.execute(f"SELECT * FROM TRANSFERENCIA WHERE NUMERO='{numero}'").fetchone()
        db.commit()
        db.close()
        return D
    
    def finalizarTransferencia(numero):
        db = conectar()
        dados_transferencia = EtapasComandoTransferir.pegarDadosTransferencia(numero)
        origem = dados_transferencia[0]
        valor = dados_transferencia[1]
        destino = dados_transferencia[2]
        saldo_final_origem = (float(InformacoesConta.pegarSaldo(origem))) - (float(valor))
        saldo_final_destino = (float(InformacoesConta.pegarSaldo(destino))) + (float(valor))
        db.executescript(f"UPDATE CONTAS SET SALDO='{saldo_final_origem}' WHERE NUMERO='{origem}'")
        db.executescript(f"UPDATE CONTAS SET SALDO='{saldo_final_destino}' WHERE NUMERO='{destino}'")
        db.commit()
        db.close()

#Gerencia informações de contas já criadas.
class InformacoesConta:
    def checarExistencia(numero):
        db = conectar()
        try:
            db = conectar()
            db.execute(f"SELECT NUMERO FROM CONTAS WHERE NUMERO='{numero}'").fetchone()[0]
            db.close()
            return True
        except:
            db.close()
            return False

    def pegarNome(numero):
        db = conectar()
        D = db.execute(f"SELECT NOME FROM CONTAS WHERE NUMERO='{numero}'").fetchone()[0]
        db.commit()
        db.close()
        return D
    
    def pegarSaldo(numero):
        db = conectar()
        D = db.execute(f"SELECT SALDO FROM CONTAS WHERE NUMERO='{numero}'").fetchone()[0]
        db.commit()
        db.close()
        return D
    
    def pegarSenha(numero):
        db = conectar()
        D = db.execute(f"SELECT SENHA FROM CONTAS WHERE NUMERO='{numero}'").fetchone()[0]
        db.commit()
        db.close()
        return D
    
    def senhaValida(numero, senha):
        if(senha == InformacoesConta.pegarSenha(numero)):
            return True
        else:
            return False
    
    def saldoSuficiente(numero, valor):
        if((float(InformacoesConta.pegarSaldo(numero))) < (float(valor)) ):
            return False
        else:
            return True
#Aqui fecha o gerenciamento do banco de dados.