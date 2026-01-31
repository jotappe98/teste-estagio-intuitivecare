Teste 2 – Transformação e Validação de Dados

Processo Seletivo – IntuitiveCare (Estágio)

Objetivo

Este projeto tem como objetivo construir um pipeline simples de processamento de dados, contemplando as etapas de:

Construção de base consolidada

Validação dos dados

Enriquecimento com cadastro da ANS (CADOP)

Agregação e geração de métricas

O foco é demonstrar organização de código, tratamento de dados e geração de saídas consistentes.


teste-2-transf-validacao-dados/
│
├── data/
│   ├── raw/         # Dados brutos 
│   └── processed/   # Bases tratadas e resultados
│
├── src/
│   ├── 01_build_base_dataset.py
│   ├── 02_validations.py
│   ├── 03_enrichments.py
│   └── 04_aggregations.py
│
├── README.md
└── requirements.txt

Descrição dos Scripts
01_build_base_dataset.py :

Responsável por carregar os arquivos de despesas e gerar a base inicial consolidada para processamento.

02_validations.py :

Realiza validações básicas nos dados, como:

Padronização de colunas

Tratamento de valores nulos

Limpeza de CNPJ

Garantia de consistência dos registros

Gera uma base validada em data/processed.

03_enrichments.py :

Realiza o enriquecimento da base de despesas com os dados do cadastro de operadoras da ANS (CADOP), utilizando o CNPJ como chave de junção.

Também é gerado um arquivo separado contendo os registros que não tiveram correspondência no CADOP.

04_aggregations.py :

Agrupa os dados por operadora (Razão Social) e UF, calculando:

Total de despesas por operadora e UF

Média de despesas

Desvio padrão das despesas

O resultado é ordenado pelo valor total de despesas (do maior para o menor) e salvo no arquivo:
data/processed/despesas_agregadas.csv

Como Executar o Projeto

Instale as dependências:

pip install -r requirements.txt

Execute os scripts na ordem:

python src/01_build_base_dataset.py
python src/02_validations.py
python src/03_enrichments.py
python src/04_aggregations.py


Trade-off Técnico (Ordenação)
A ordenação dos dados foi realizada diretamente com o Pandas após a agregação, utilizando sort_values.

Essa abordagem foi escolhida por ser simples, legível e suficiente para o volume de dados utilizado neste teste. Em um cenário com volumes muito maiores, poderia ser avaliada a utilização de bancos de dados ou processamento distribuído para melhorar performance e consumo de memória.

Observações Finais

O pipeline foi estruturado de forma sequencial para facilitar entendimento e manutenção.

O projeto prioriza clareza e organização do código.

Todas as saídas são salvas na pasta data/processed para facilitar a verificação dos resultados.