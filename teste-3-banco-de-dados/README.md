# Teste 3 – Banco de Dados (SQL)

## Objetivo
Este teste tem como objetivo demonstrar a criação de estruturas de banco de dados e consultas SQL a partir dos dados gerados nos testes anteriores.

O foco está em:
- Modelagem simples de tabelas
- Carga de dados a partir de arquivos CSV
- Escrita de queries analíticas básicas

## Descrição dos Arquivos

### 01_create_tables.sql
Cria a tabela `despesas_operadoras`, utilizada para armazenar os dados agregados de despesas por operadora e UF.

### 02_insert_data.sql
Contém comandos de inserção de dados de exemplo, simulando a carga dos dados provenientes dos arquivos CSV gerados nos testes anteriores.

### 03_queries.sql
Reúne consultas analíticas simples, como:
- Listagem de operadoras por total de despesas
- Ranking das operadoras com maiores gastos
- Distribuição de despesas por UF
- Filtros por média trimestral

