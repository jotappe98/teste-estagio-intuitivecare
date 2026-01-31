"""
Este script realiza:
- Agregação de despesas por operadora e UF
- Cálculo de total, média trimestral e desvio padrão
- Ordenação por valor total (decrescente)
"""

import pandas as pd

INPUT_PATH = "data/processed/despesas_operadoras_enriquecido.csv"
OUTPUT_PATH = "data/processed/despesas_agregadas.csv"

print("Carregando base enriquecida...")

df = pd.read_csv(
    INPUT_PATH,
    sep=";",
    encoding="utf-8"
)

print(f"Registros carregados: {df.shape}")

# Padronização
df.columns = df.columns.str.strip().str.upper()

# Garantir tipo numérico
df["VALOR_TOTAL_VL_SALDO_FINAL"] = pd.to_numeric(
    df["VALOR_TOTAL_VL_SALDO_FINAL"],
    errors="coerce"
)


# Agregações
print("Realizando agregações por operadora e UF...")

df_agregado = (
    df
    .groupby(["RAZAO_SOCIAL", "UF"])
    .agg(
        TOTAL_DESPESAS=("VALOR_TOTAL_VL_SALDO_FINAL", "sum"),
        MEDIA_TRIMESTRAL=("VALOR_TOTAL_VL_SALDO_FINAL", "mean"),
        DESVIO_PADRAO=("VALOR_TOTAL_VL_SALDO_FINAL", "std")
    )
    .reset_index()
)

# Ordenação
df_agregado = df_agregado.sort_values(
    by="TOTAL_DESPESAS",
    ascending=False
)

print(f"Base agregada gerada: {df_agregado.shape}")

# Salvar resultado
df_agregado.to_csv(
    OUTPUT_PATH,
    sep=";",
    index=False,
    encoding="utf-8"
)

print(f"Arquivo salvo em: {OUTPUT_PATH}")
