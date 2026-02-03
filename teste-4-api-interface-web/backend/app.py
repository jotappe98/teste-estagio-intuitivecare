from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Carrega dados
df = pd.read_csv(
    "data/despesas_agregadas.csv",
    sep=";",
    encoding="utf-8"
)

@app.route("/api/operadoras", methods=["GET"])
def listar_operadoras():
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
