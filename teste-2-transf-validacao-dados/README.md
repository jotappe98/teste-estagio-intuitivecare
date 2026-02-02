Teste 2 – Transformação e Validação de Dados

Processo Seletivo – IntuitiveCare (Estágio)

Objetivo

Este projeto tem como objetivo realizar a transformação e validação dos dados consolidados no Teste 1, aplicando um pipeline simples e organizado que contempla:

Construção de uma base inicial para análise

Validação de consistência dos dados

Enriquecimento com dados cadastrais da ANS (CADOP)

Agregação e geração de métricas analíticas

O foco está em demonstrar organização de código, tratamento de dados e tomada de decisões técnicas adequadas ao contexto do problema.

Descrição dos Scripts
01_build_base_dataset.py

Responsável por carregar os dados consolidados de despesas (gerados no Teste 1) e o cadastro de operadoras da ANS (CADOP), criando uma base intermediária para processamento posterior.

Essa etapa tem como objetivo preparar os dados para as validações e enriquecimentos seguintes, mantendo o pipeline organizado em fases bem definidas.

02_validations.py

Realiza validações básicas para garantir a consistência dos dados, incluindo:

Padronização dos nomes das colunas

Remoção de registros com Razão Social vazia

Conversão e validação de valores monetários positivos

Validação de CNPJ (formato e dígitos verificadores)

Os registros que não atendem aos critérios definidos são removidos, e o resultado é salvo como uma base validada em data/processed.

03_enrichments.py

Executa o enriquecimento da base validada de despesas com os dados cadastrais das operadoras da ANS (CADOP), utilizando o CNPJ como chave de junção.

Também é gerado um arquivo separado contendo os registros que não tiveram correspondência no cadastro, permitindo análise posterior de possíveis inconsistências ou lacunas nos dados.

04_aggregations.py

Realiza a agregação dos dados por operadora (Razão Social) e UF, calculando:

Total de despesas

Média de despesas

Desvio padrão das despesas

O resultado é ordenado pelo valor total de despesas (do maior para o menor) e salvo no arquivo:
data/processed/despesas_agregadas.csv

Como Executar o Projeto

Instale as dependências:
pip install -r requirements.txt

Execute os scripts na ordem abaixo:

python src/01_build_base_dataset.py
python src/02_validations.py
python src/03_enrichments.py
python src/04_aggregations.py

Trade-offs Técnicos
Validação de CNPJ

Durante o processamento, foram identificados CNPJs inválidos.
As alternativas consideradas incluíam manter os registros marcados como inválidos ou separá-los em uma base auxiliar.

Optou-se por remover os registros inválidos do pipeline principal para garantir consistência nas etapas de enriquecimento e agregação, simplificando o fluxo de processamento.

Estratégia de Join com o CADOP

Foi utilizado um LEFT JOIN entre a base de despesas e o cadastro de operadoras, garantindo que registros de despesas sem correspondência no CADOP não fossem descartados silenciosamente. Esses casos são registrados em um arquivo separado para análise.

Ordenação dos Dados

A ordenação dos dados agregados foi realizada utilizando sort_values do Pandas, após a etapa de agregação.

Essa abordagem foi escolhida por ser simples, legível e adequada ao volume de dados utilizado neste teste. Em cenários com volumes significativamente maiores, outras soluções poderiam ser avaliadas, como o uso de bancos de dados ou processamento distribuído.

Observações Finais

O pipeline foi estruturado de forma sequencial para facilitar o entendimento e a manutenção do código.
As decisões técnicas priorizaram simplicidade, clareza e aderência ao escopo do teste, evitando complexidade desnecessária.

Todas as saídas geradas são salvas na pasta data/processed, facilitando a verificação dos resultados.