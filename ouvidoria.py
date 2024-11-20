from operacoesbd import * 

def listar_manifestacoes(connection):
  query = "SELECT * FROM manifestacoes"
  manifestacoes = listarBancoDados(connection, query)

  if manifestacoes:
    for manifestacao in manifestacoes:
      print("ID", manifestacao[0], "-", manifestacao[1], "-", manifestacao[2])
  else:
    print("Nenhuma manifestação cadastrada no sistema.")