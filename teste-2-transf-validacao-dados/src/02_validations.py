"""
Este script realiza:
- Padronização das colunas
- Validação de CNPJ (formato e dígitos verificadores)
- Validação de valores numéricos positivos
- Validação de Razão Social não vazia
- Tratamento de CNPJs inválidos (estratégia documentável no README)
"""

import pandas as pd
import re

# Funções Auxiliares


def limpar_cnpj(cnpj: str) -> str:
    """Remove caracteres não numéricos do CNPJ."""
    return re.sub(r"\D", "", str(cnpj))


def cnpj_valido(cnpj: str) -> bool:
    """
    Valida CNPJ considerando:
    - Quantidade de dígitos
    - Dígitos verificadores
    """
    cnpj = limpar_cnpj(cnpj)

    if len(cnpj) != 14:
        return False

    if cnpj == cnpj[0] * 14:
        return False

    def calcular_digito(cnpj_parcial, pesos):
        soma = sum(int(d) * p for d, p in zip(cnpj_parcial, pesos))
        resto = soma % 11
        return "0" if resto < 2 else str(11 - resto)

    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [6] + pesos_1

    digito_1 = calcular_digito(cnpj[:12], pesos_1)
    digito_2 = calcular_digito(cnpj[:12] + digito_1, pesos_2)

    return cnpj[-2:] == digito_1 + digito_2






df = pd.read_csv(
    "data/processed/despesas_operadoras_base.csv",
    sep=";",
    encoding="utf-8"
)

print(f"Registros carregados: {df.shape}")


# Padronização de colunas
df.columns = (
    df.columns
    .str.strip()
    .str.upper()
)

# ----------------------------
# Validação: Razão Social
# ----------------------------
print("Validando Razão Social:")

registros_antes = len(df)
df = df.dropna(subset=["RAZAO_SOCIAL"])
registros_depois = len(df)

print(f"Registros removidos por Razão Social vazia: {registros_antes - registros_depois}")


# Validação: Valores numéricos positivos
print("Validando valores monetários:")

df["VALOR_TOTAL_VL_SALDO_FINAL"] = pd.to_numeric(
    df["VALOR_TOTAL_VL_SALDO_FINAL"],
    errors="coerce"
)

registros_antes = len(df)
df = df[df["VALOR_TOTAL_VL_SALDO_FINAL"] > 0]
registros_depois = len(df)

print(f" Registros removidos por valor inválido: {registros_antes - registros_depois}")


# Validação CNPJ
print("Validando CNPJs:")

df["CNPJ_LIMPO"] = df["CNPJ"].apply(limpar_cnpj)
df["CNPJ_VALIDO"] = df["CNPJ_LIMPO"].apply(cnpj_valido)

qtd_invalidos = (~df["CNPJ_VALIDO"]).sum()

print(f" CNPJs inválidos encontrados: {qtd_invalidos}")


# Remover registros com CNPJ inválido
df = df[df["CNPJ_VALIDO"]]

print(f"✔ Registros após validação de CNPJ: {df.shape}")


# Limpeza 
df = df.drop(columns=["CNPJ_LIMPO", "CNPJ_VALIDO"])


# Salva o resultado
output_path = "data/processed/despesas_operadoras_validado.csv"

df.to_csv(
    output_path,
    sep=";",
    index=False,
    encoding="utf-8"
)

print(f" Arquivo salvo em: {output_path}")
print(" Etapa 2.1 concluída com sucesso.")