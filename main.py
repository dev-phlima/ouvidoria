from ouvidoria import *
from operacoesbd import criarConexao

connection = criarConexao("localhost", "root", "root", "ouvidoria")

opcao_usuario = -1

while opcao_usuario != 7:
    print(
        "1) Listagem das Manifestações\n2) Listagem de Manifestações por Tipo\n3) Criar uma Nova Manifestação\n4) Exibir Quantidade de Manifestações\n5) Pesquisar uma Manifestação por Código\n6) Excluir uma Manifestação pelo Código\n7) Sair do Sistema")
    opcao_usuario = int(input("Digite sua opção: "))

    if opcao_usuario == 1:
        listar_manifestacoes(connection)


    elif opcao_usuario == 2:
        print("\n1) Elogios", "\n2) Reclamações", "\n3) Susgestão")
        opcao = int(input('Digite sua opção: '))
        tiporeclamacao = None
        if opcao == 1:
            tiporeclamacao = "select * from manifestacoes where tipo_manifestacao = 'Elogio'"
        elif opcao == 2:
            tiporeclamacao = "select * from manifestacoes where tipo_manifestacao = 'Reclamação'"
        elif opcao == 3:
            tiporeclamacao = "select * from manifestacoes where tipo_manifestacao = 'Sugestão'"

        if tiporeclamacao != None:
            listarPorTipo(connection, tiporeclamacao)
        else:
            print("Nenhuma manifestação encontrada com o tipo especificado.")


    elif opcao_usuario == 3:
        print("\n1) Fazer Elogios", "\n2) Fazer Reclamações", "\n3) Fazer Susgestão")
        opcao = int(input("Digite o número do tipo de manifestação desejado: "))
        tipo_manifestacao = None
        if opcao == 1:
            tipo_manifestacao = "Elogio"
        elif opcao == 2:
            tipo_manifestacao = "Reclamação"
        elif opcao == 3:
            tipo_manifestacao = "Sugestão"

        if tipo_manifestacao != None:
            manifestacao = input("Digite sua manifestação desejada: ")
            insertManifestion(connection, manifestacao, tipo_manifestacao)
        else:
            print("Tipo de Manifestação inválida!")


    elif opcao_usuario == 4:
        contar_total_manifestacoes(connection)


    elif opcao_usuario == 5:
        codigo = int(input("Digite o código da manifestação desejada: "))
        pesquisar_por_codigo(connection, codigo)
