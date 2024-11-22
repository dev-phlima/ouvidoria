from operacoesbd import *

"""
Para a criação do banco de dados e sua tabela, nós utilizamos da seguinte instrução: 

CREATE DATABASE ouvidoria;

USE ouvidoria; 

CREATE TABLE manifestacoes (
    id_manifestacao INT AUTO_INCREMENT NOT NULL,
    manifestacao TEXT NOT NULL,                      
    tipo_manifestacao ENUM('Elogio', 'Reclamação', 'Sugestão') NOT NULL,
    PRIMARY KEY (id_manifestacao)
);
"""

def listar_manifestacoes(connection):
    query = "SELECT * FROM manifestacoes"
    manifestacoes = listarBancoDados(connection, query)

    if manifestacoes:
        for manifestacao in manifestacoes:
            print("ID", manifestacao[0], "-", manifestacao[1], "-", manifestacao[2])
    else:
        print("Nenhuma manifestação cadastrada no sistema.")


def contar_total_manifestacoes(connection):
    quantidade_de_manifestacoes = listarBancoDados(connection, "SELECT COUNT(*) FROM manifestacoes")
    if quantidade_de_manifestacoes:
        print("Número total de manifestações:", quantidade_de_manifestacoes[0][0])
    else:
        print("Nenhuma manifestação registrada no sistema.")


def inserir_manifestacao(connection, manifestacao, tipo_manifestacao):
    query = "INSERT INTO manifestacoes (manifestacao,tipo_manifestacao) VALUES (%s ,%s)"
    values = [manifestacao, tipo_manifestacao]
    insertNoBancoDados(connection, query, values)
    print("Manifestação cadastrada com sucesso.")


def listar_por_tipo(connection, tipo_reclamacao):
    manifestacoes = listarBancoDados(connection, tipo_reclamacao)
    if manifestacoes:
        for manifestacao in manifestacoes:
            print("ID", manifestacao[0], "-", manifestacao[1], "-", manifestacao[2])
    else:
        print("Nenhuma manifestação encontrada no sistema com o tipo fornecido.")


def pesquisar_por_codigo(connection, codigo):
    query = "SELECT * FROM manifestacoes WHERE id_manifestacao = %s"
    dados = [codigo]
    tupla_manifestacao = listarBancoDados(connection, query, dados)

    if tupla_manifestacao:
        print("ID", tupla_manifestacao[0][0], "-", tupla_manifestacao[0][1], "-", tupla_manifestacao[0][2])
    else:
        print("Nenhuma manifestação encontrada com o código especificado.")


def excluir_por_codigo(connection, codigo_excluir):
    query = "DELETE FROM manifestacoes WHERE id_manifestacao = %s"
    dados = [codigo_excluir]
    linhas_afetadas = excluirBancoDados(connection, query, dados)
    if linhas_afetadas > 0:
        print("Manifestação removida com sucesso!")
    else:
        print("Não existe manifestação com esse código!")
