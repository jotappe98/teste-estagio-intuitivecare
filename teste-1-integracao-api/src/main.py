from pathlib import Path
import csv
import unicodedata
from collections import defaultdict



# Configurações

DATA_DIR = Path("data/raw")
FILES = ["1T2025.csv", "2T2025.csv", "3T2025.csv"]

KEYWORDS = ["SINISTRO", "EVENTO", "ASSISTENCIAL"]

# Funções auxiliares

def normalize_text(text: str) -> str: #Remove acentos e converte o texto para maiúsculo
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ASCII", "ignore").decode("ASCII")
    return text.upper()


def read_csv_safe(path: Path): #Tenta abrir CSV com utf-8, se falhar usa latin-1
    try:
        return open(path, mode="r", encoding="utf-8")
    except UnicodeDecodeError:
        return open(path, mode="r", encoding="latin-1")


def classify_account(descricao_normalizada: str) -> str: #Classifica o tipo de conta com base na descrição
    if "COBERTURA ASSISTENCIAL" in descricao_normalizada:
        return "COBERTURA_ASSISTENCIAL"
    elif "PROVISAO" in descricao_normalizada:
        return "PROVISAO_SINISTROS"
    elif "INDENIZACAO" in descricao_normalizada:
        return "INDENIZACOES"
    elif "RECEITA" in descricao_normalizada:
        return "RECEITAS_SINISTROS"
    else:
        return "OUTROS_EVENTOS_SINISTROS"


# Processamento de Arquivos

all_records = []
count_by_trimester = defaultdict(int)

for file_name in FILES:
    file_path = DATA_DIR / file_name
    trimester = file_name.replace(".csv", "")

    with read_csv_safe(file_path) as f:
        reader = csv.DictReader(f, delimiter=";")

        for row in reader:
            descricao = row.get("DESCRICAO", "")
            descricao_norm = normalize_text(descricao)

            if any(k in descricao_norm for k in KEYWORDS):
                row["TRIMESTRE"] = trimester
                row["TIPO_CONTA"] = classify_account(descricao_norm)

                all_records.append(row)
                count_by_trimester[trimester] += 1


# Resultado — quantidade por trimestre

print(f"\nTotal geral de registros filtrados: {len(all_records)}\n")

for trimester, count in count_by_trimester.items():
    print(f"{trimester}: {count}")



# Agregação — VL_SALDO_FINAL por trimestre

total_by_trimester = defaultdict(float)

for row in all_records:
    trimester = row["TRIMESTRE"]
    value_raw = row.get("VL_SALDO_FINAL", "").strip()

    if value_raw == "":
        continue

    try:
        value = float(value_raw)
    except ValueError:
        continue

    total_by_trimester[trimester] += value


print("\nValor total de VL_SALDO_FINAL por trimestre:\n")

for trimester, total in total_by_trimester.items():
    print(f"{trimester}: {total:.2f}")



# Validação — exemplos por tipo de conta
examples_by_type = defaultdict(list)

for row in all_records:
    tipo = row["TIPO_CONTA"]
    if len(examples_by_type[tipo]) < 5:
        examples_by_type[tipo].append(
            (row["CD_CONTA_CONTABIL"], row["DESCRICAO"])
        )

print("\nExemplos por TIPO_CONTA:\n")

for tipo, examples in examples_by_type.items():
    print(f"{tipo}:")
    for code, desc in examples:
        print(f"  {code} - {desc}")
    print()


# Agregação — TRIMESTRE + TIPO_CONTA
total_by_trimester_and_type = defaultdict(float)

for row in all_records:
    trimester = row["TRIMESTRE"]
    tipo = row["TIPO_CONTA"]
    value_raw = row.get("VL_SALDO_FINAL", "").strip()

    if value_raw == "":
        continue

    try:
        value = float(value_raw)
    except ValueError:
        continue

    key = (trimester, tipo)
    total_by_trimester_and_type[key] += value



# Resultado — agregação detalhada
print("\nValor total por TRIMESTRE e TIPO_CONTA:\n")

for (trimester, tipo), total in sorted(total_by_trimester_and_type.items()):
    print(f"{trimester} | {tipo} | {total:.2f}")



# Exportação CSV 
OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "ans_sinistros_agregado.csv"

with open(OUTPUT_FILE, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    
    writer.writerow([
        "TRIMESTRE",
        "TIPO_CONTA",
        "VALOR_TOTAL_VL_SALDO_FINAL"
    ])
    
    for (trimester, tipo_conta), total in total_by_trimester_and_type.items():
        writer.writerow([
            trimester,
            tipo_conta,
            f"{total:.2f}"
        ])

print(f"\nCSV gerado com sucesso em: {OUTPUT_FILE}")