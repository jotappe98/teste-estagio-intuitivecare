FONTE DOS DADOS

Foram utilizadas as Demonstrações Contábeis da ANS referentes aos 3 trimestres do ano de 2025:

1T2025
2T2025
3T2025

Esses arquivos foram selecionados por representarem os dados mais recentes disponíveis no momento da realização do teste e por apresentarem uma estrutura consistente para análise.

Os arquivos originais foram obtidos a partir do portal de Dados Abertos da ANS:

🔗 https://dadosabertos.ans.gov.br/FTP/PDA/

 ESTRATÉGIA DE PROCESSAMENTO

Foi adotada uma estratégia de processamento incremental, lendo os arquivos CSV linha a linha, em vez de carregar todos os dados integralmente em memória.

Justificativa do trade-off técnico

Os arquivos de Demonstrações Contábeis da ANS podem ter volume elevado

O processamento incremental reduz o consumo de memória

Permite filtragem e agregação durante a leitura

Facilita a execução em ambientes com recursos limitados

 IDENTIFICAÇÃO DE EVENTOS E SINISTROS

Os registros relacionados a Despesas com Eventos/Sinistros foram identificados por meio da análise da coluna DESCRICAO, utilizando palavras-chave relevantes:

SINISTRO

EVENTO

ASSISTENCIAL

Antes da verificação, o texto da descrição é normalizado (remoção de acentos e conversão para maiúsculas), reduzindo inconsistências causadas por variações de escrita.

Além disso, os registros filtrados são classificados em tipos de conta contábil, como:

Cobertura Assistencial

Provisão de Sinistros

Receitas de Sinistros

Outros Eventos/Sinistros

 TRATAMENTO DE INCONSISTÊNCIAS

Durante o processamento e consolidação dos dados, as seguintes situações foram tratadas:

🔹 CNPJs duplicados com razões sociais diferentes

Os arquivos de Demonstrações Contábeis da ANS não contêm informações de CNPJ ou Razão Social, apresentando apenas dados contábeis agregados e o identificador REG_ANS.

Dessa forma, essa inconsistência não se aplica nesta etapa do teste, sendo tratada apenas nos testes posteriores, onde são utilizados os dados cadastrais das operadoras.

🔹 Valores vazios, zerados ou inválidos

Registros com valores vazios ou não numéricos na coluna VL_SALDO_FINAL foram ignorados

Essa decisão evita a introdução de ruído nos valores consolidados

Valores negativos, quando presentes, foram mantidos por poderem representar ajustes contábeis legítimos

🔹 Inconsistência nos formatos de data

Para evitar problemas relacionados a diferentes formatos de data nos arquivos, o trimestre e o ano foram inferidos a partir do nome dos arquivos de origem (ex.: 1T2025, 2T2025, 3T2025).

Essa abordagem garante consistência na identificação dos períodos analisados.

 CONSOLIDAÇÃO DOS DADOS

Os dados filtrados foram consolidados em um único arquivo CSV contendo informações agregadas por:

Trimestre

Tipo de conta contábil

Arquivo final gerado:

consolidado_despesas.csv

Conforme solicitado no enunciado, o CSV final foi compactado no arquivo:

consolidado_despesas.zip

 COMO EXECUTAR

Navegue até a pasta do projeto

Execute o comando:

python src/main.py


O arquivo processado será gerado automaticamente na pasta data/processed/ e compactado conforme especificado.

 CONSIDERAÇÕES FINAIS

As decisões técnicas adotadas priorizam:

Fidelidade aos dados originais disponibilizados pela ANS

Simplicidade e clareza da solução

Tratamento explícito de limitações do dataset

Facilidade de evolução para as próximas etapas do teste
