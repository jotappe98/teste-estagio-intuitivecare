from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Lê e carrega os dados
df = pd.read_csv(
    "backend/data/despesas_agregadas.csv",
    sep=";",
    encoding="utf-8"
)

# Rota para listar as operadoras
@app.route("/api/operadoras", methods=["GET"])
def listar_operadoras():
    # parâmetros de paginação
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    dados_paginados = df.iloc[start:end]

    return jsonify({
        "data": dados_paginados.to_dict(orient="records"),
        "page": page,
        "limit": limit,
        "total": len(df)
    })

if __name__ == "__main__":
    app.run(debug=True)
