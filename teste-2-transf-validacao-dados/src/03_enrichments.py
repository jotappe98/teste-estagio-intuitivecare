"""
Este script realiza:
- Carrega a base validada de despesas
- Carrega o cadastro de operadoras ativas (ANS)
- Realiza join por CNPJ
- Trata registros sem match e duplicidades
"""

import pandas as pd
import re



# Funções auxiliares

def limpar_cnpj(cnpj: str) -> str:
    """Remove caracteres não numéricos do CNPJ."""
    return re.sub(r"\D", "", str(cnpj))



# Carga dos dados

print("Carregando base de despesas validada...")

df_despesas = pd.read_csv(
    "data/processed/despesas_operadoras_validado.csv",
    sep=";",
    encoding="utf-8"
)

print(f"Despesas carregadas: {df_despesas.shape}")

print("Carregando cadastro de operadoras (CADOP)...")

df_cadop = pd.read_csv(
    "data/raw/Relatorio_cadop.csv",
    sep=";",
    encoding="latin1"
)

print(f"Operadoras carregadas: {df_cadop.shape}")


# Padronização

df_despesas.columns = df_despesas.columns.str.strip().str.upper()
df_cadop.columns = df_cadop.columns.str.strip().str.upper()

df_despesas["CNPJ"] = df_despesas["CNPJ"].apply(limpar_cnpj)
df_cadop["CNPJ"] = df_cadop["CNPJ"].apply(limpar_cnpj)



# Deduplicação do cadastro

print("Removendo duplicidades no CADOP...")

qtd_antes = len(df_cadop)
df_cadop = df_cadop.drop_duplicates(subset=["CNPJ"])
qtd_depois = len(df_cadop)

print(f"Duplicatas removidas: {qtd_antes - qtd_depois}")



# Seleção e padronização de colunas

df_cadop = df_cadop[
    [
        "CNPJ",
        "REGISTRO_OPERADORA",
        "MODALIDADE",
        "UF"
    ]
]

# Padroniza o nome 
df_cadop = df_cadop.rename(columns={
    "REGISTRO_OPERADORA": "REGISTRO_ANS"
})



# JOIN 

print("Realizando enriquecimento por CNPJ (LEFT JOIN)...")

df_enriquecido = df_despesas.merge(
    df_cadop,
    on="CNPJ",
    how="left"
)

print(f"Base enriquecida: {df_enriquecido.shape}")



# Análise de falhas de match


sem_match = df_enriquecido["REGISTRO_ANS"].isna().sum()

print(f"Registros sem correspondência no CADOP: {sem_match}")



# Salva o resultado

output_path = "data/processed/despesas_operadoras_enriquecido.csv"

df_enriquecido.to_csv(
    output_path,
    sep=";",
    index=False,
    encoding="utf-8"
)

print(f"Arquivo salvo em: {output_path}")
