from ouvidoria import * 
from operacoesbd import criarConexao

connection = criarConexao("localhost", "root", "snoopy", "ouvidoria")

opcao_usuario = -1 

while opcao_usuario != 7:
  print("1) Listagem das Manifestações\n2) Listagem de Manifestações por Tipo\n3) Criar uma Nova Manifestação\n4) Exibir Quantidade de Manifestações\n5) Pesquisar uma Manifestação por Código\n6) Excluir uma Manifestação pelo Código\n7) Sair do Sistema")
  opcao_usuario = int(input("Digite sua opção: "))

  if opcao_usuario == 1:
    listar_manifestacoes(connection)



  elif opcao_usuario == 4:
    contar_total_manifestacoes(connection)