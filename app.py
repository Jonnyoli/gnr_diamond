from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/registrar_servico", methods=["POST"])
def registrar_servico():
    dados = request.json
    print("✅ Dados recebidos:", dados)
    return jsonify({
        "status": "ok",
        "mensagem": "Dados recebidos com sucesso!"
    })