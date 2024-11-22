from ouvidoria import *
from operacoesbd import criarConexao

connection = criarConexao("localhost", "root", "19122005Pe", "ouvidoria")

opcao_usuario = -1

while opcao_usuario != 7:
    print("1) Listagem das Manifestações\n2) Listagem de Manifestações por Tipo\n3) Criar uma Nova Manifestação\n4) Exibir Quantidade de Manifestações\n5) Pesquisar uma Manifestação por Código\n6) Excluir uma Manifestação pelo Código\n7) Sair do Sistema")
    opcao_usuario = int(input("Digite a opção desejada: "))
    print()

    if opcao_usuario == 1:
        listar_manifestacoes(connection)
        print()

    elif opcao_usuario == 2:
        print("1) Elogios\n2) Reclamações\n3) Sugestão")
        opcao = int(input('Indique o tipo das manifestações que você deseja listar: '))
        tipo_reclamacao = None
        if opcao == 1:
            tipo_reclamacao = "SELECT * FROM manifestacoes WHERE tipo_manifestacao = 'Elogio'"
        elif opcao == 2:
            tipo_reclamacao = "SELECT * FROM manifestacoes WHERE tipo_manifestacao = 'Reclamação'"
        elif opcao == 3:
            tipo_reclamacao = "SELECT * FROM manifestacoes WHERE tipo_manifestacao = 'Sugestão'"

        if tipo_reclamacao != None:
            listar_por_tipo(connection, tipo_reclamacao)
            print()
        else:
            print("Indique um tipo válido.")
            print()

    elif opcao_usuario == 3:
        print("1) Tecer elogio\n2) Fazer reclamação\n3) Fazer uma sugestão")
        opcao = int(input("Qual é o gênero da sua manifestação: "))
        tipo_manifestacao = None
        if opcao == 1:
            tipo_manifestacao = "Elogio"
        elif opcao == 2:
            tipo_manifestacao = "Reclamação"
        elif opcao == 3:
            tipo_manifestacao = "Sugestão"

        if tipo_manifestacao != None:
            manifestacao = input("Faça sua manifestação: ")
            inserir_manifestacao(connection, manifestacao, tipo_manifestacao)
            print()
        else:
            print("Tipo de Manifestação inválida!")
            print()

    elif opcao_usuario == 4:
        contar_total_manifestacoes(connection)
        print()

    elif opcao_usuario == 5:
        codigo_pesquisa = int(input("Digite o código da manifestação desejada: "))
        pesquisar_por_codigo(connection, codigo_pesquisa)
        print()

    elif opcao_usuario == 6:
        codigo_excluir = int(input("Digite o código da manifestação que você deseja excluir: "))
        excluir_por_codigo(connection, codigo_excluir)
        print()
    
    elif opcao_usuario != 7:
        print("Digite uma opção válida.")
        print()

