# Sistema de Ouvidoria

Este projeto é um sistema de ouvidoria que permite o gerenciamento de manifestações, como elogios, reclamações e sugestões. Ele possibilita a listagem, criação, pesquisa e exclusão de manifestações, além de exibir a quantidade total registrada. O sistema se conecta a um banco de dados MySQL para armazenar e gerenciar as informações.

## Arquivos do Projeto

- `main.py`: Arquivo principal que executa o sistema e gerencia as interações do usuário com o menu.
- `operacoesbd.py`: Define as funções para conexão e manipulação de dados no banco de dados MySQL.
- `ouvidoria.py`: Contém as funções de gerenciamento das manifestações.

## Funcionalidades

1. **Listagem de Manifestações**: Lista todas as manifestações cadastradas.
2. **Listagem de Manifestações por Tipo**: Filtra manifestações por tipo (`Elogio`, `Reclamação`, `Sugestão`).
3. **Criação de Manifestação**: Adiciona uma nova manifestação ao sistema.
4. **Exibição da Quantidade de Manifestações**: Mostra o número total de manifestações cadastradas.
5. **Pesquisa de Manifestação por Código**: Busca uma manifestação específica pelo código.
6. **Exclusão de Manifestação pelo Código**: Exclui uma manifestação com base no código informado.

## Pré-requisitos

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python` para Python (pode ser instalada via `pip install mysql-connector-python`)

## Configuração

1. Certifique-se de que o MySQL Server está em execução e que você possui um banco de dados chamado `ouvidoria`.
2. Configure as credenciais de conexão no arquivo `main.py` na função `criarConexao`.

Exemplo de configuração:
```python
connection = criarConexao("localhost", "usuario", "senha", "ouvidoria")
