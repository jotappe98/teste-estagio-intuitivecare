from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Base principal (detalhada)
df_operadoras = pd.read_csv(
    "backend/data/despesas_operadoras_enriquecido.csv",
    sep=";",
    encoding="utf-8"
)

df_operadoras["CNPJ"] = df_operadoras["CNPJ"].astype(str)  #Transforma o dado recebido do csv em str

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


# Rota para encontrar operadora por CNPJ
@app.route("/api/operadoras/<cnpj>", methods=["GET"])
def get_operadora_por_cnpj(cnpj):
    print("CNPJ recebido na rota:", cnpj, type(cnpj))
    print(
        "CNPJ no dataframe:",
        df_operadoras["CNPJ"].iloc[0],
        type(df_operadoras["CNPJ"].iloc[0])
    )

    operadora = df_operadoras[df_operadoras["CNPJ"] == cnpj]

    if operadora.empty:
        return jsonify({"erro": "Operadora não encontrada"}), 404

    return jsonify(operadora.to_dict(orient="records"))



if __name__ == "__main__":
    app.run(debug=True)
