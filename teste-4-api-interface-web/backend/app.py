from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Base principal (detalhada)
df_operadoras = pd.read_csv(
    "backend/data/despesas_operadoras_enriquecido.csv",
    sep=";",
    encoding="utf-8"
)

# Base agregada (estatísticas)
df_agregado = pd.read_csv(
    "backend/data/despesas_agregadas.csv",
    sep=";",
    encoding="utf-8"
)

# Rota para listar as operadoras
@app.route("/api/operadoras", methods=["GET"])
def listar_operadoras():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    # Remove duplicatas por CNPJ 
    operadoras_unicas = df_operadoras.drop_duplicates(subset=["CNPJ"])

    dados_paginados = operadoras_unicas.iloc[start:end]

    return jsonify({
        "data": dados_paginados.to_dict(orient="records"),
        "page": page,
        "limit": limit,
        "total": len(operadoras_unicas)
    })


# Rota para obter detalhes de uma operadora específica
@app.route("/api/operadoras/<cnpj>", methods=["GET"])
def detalhe_operadora(cnpj):
    operadora = df[df["CNPJ"] == cnpj]

    if operadora.empty:
        return jsonify({"erro": "Operadora não encontrada"}), 404

    return jsonify(operadora.to_dict(orient="records")[0])


if __name__ == "__main__":
    app.run(debug=True)
