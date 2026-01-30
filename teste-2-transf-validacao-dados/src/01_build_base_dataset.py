import pandas as pd
from pathlib import Path

# Definição de caminhos do projeto

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

CONSOLIDADO_PATH = PROCESSED_DIR / "consolidado_despesas.csv"
CADOP_PATH = RAW_DIR / "Relatorio_cadop.csv"
OUTPUT_PATH = PROCESSED_DIR / "despesas_operadoras_base.csv"



# Carregamento dos dados

print("Iniciando carregamento dos dados...")

df_despesas = pd.read_csv(
    CONSOLIDADO_PATH,
    sep=";",
    encoding="utf-8"
)

df_cadop = pd.read_csv(
    CADOP_PATH,
    sep=";",
    encoding="latin1"
)

print(f"Despesas consolidadas carregadas: {df_despesas.shape}")
print(f"Cadastro de operadoras carregado: {df_cadop.shape}")



# Seleção e padronização das colunas

print("Selecionando colunas relevantes...")

df_despesas = df_despesas[
    [
        "TRIMESTRE",
        "TIPO_CONTA",
        "VALOR_TOTAL_VL_SALDO_FINAL"
    ]
]

df_cadop = df_cadop[
    [
        "REGISTRO_OPERADORA",
        "CNPJ",
        "Razao_Social",
        "Modalidade",
        "UF"
    ]
]


# Construção da base analítica
print("Construindo base analítica (produto cartesiano)...")

df_despesas["key"] = 1
df_cadop["key"] = 1

df_base = (
    pd.merge(df_cadop, df_despesas, on="key")
      .drop(columns="key")
)

print(f"Base analítica gerada com sucesso: {df_base.shape}")



# Salva o resultado
df_base.to_csv(
    OUTPUT_PATH,
    sep=";",
    index=False,
    encoding="utf-8"
)

print("Processamento concluído.")
print(f"Arquivo gerado em: {OUTPUT_PATH}")