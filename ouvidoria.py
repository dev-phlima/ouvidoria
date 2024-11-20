from operacoesbd import *

def listar_manifestacoes(connection):
  query = "SELECT * FROM manifestacoes"
  manifestacoes = listarBancoDados(connection, query)

  if manifestacoes:
    for manifestacao in manifestacoes:
      print("ID", manifestacao[0], "-", manifestacao[1], "-", manifestacao[2])
  else:
    print("Nenhuma manifestação cadastrada no sistema.")

def contar_total_manifestacoes(connection):
    quantidade_de_manifestacoes = listarBancoDados(connection, "SELECT count(*) FROM manifestacoes")
    if quantidade_de_manifestacoes:
      print("Número total de manifestações:", quantidade_de_manifestacoes[0][0])
    else:
      print("Nenhuma manifestação registrada no sistema.")

def insertManifestion(connection,manifestacao,tipo_manifestacao):
        query= "insert into manifestacoes (manifestacao,tipo_manifestacao) values (%s ,%s)"
        values=[manifestacao,tipo_manifestacao]
        insertNoBancoDados(connection,query,values)

def listarPorTipo(connection,tiporeclamacao):
    manifestacoes = listarBancoDados(connection, tiporeclamacao)
    if manifestacoes:
        for manifestacao in manifestacoes:
            print("ID", manifestacao[0], "-", manifestacao[1], "-", manifestacao[2])
    else:
        print("Nenhuma manifestção cadastrada no sistema")