import json
from flask import Flask

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def home():
    componente = "orchestracao"
    desc = "orquestra todas as comunicacoes"
    ver = "0.1"
    out = {
        "componente": componente,
        "descricao": desc,
        "versao": ver
    }
    return json.dumps(out)


def main():
    app.run(host='0.0.0.0', port=3002)


if __name__ == "__main__":
    main()
