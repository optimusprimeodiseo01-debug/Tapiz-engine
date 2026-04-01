from flask import Flask, request, jsonify
from engine.executor import Executor
from integration.github_listener import GitHubListener

app = Flask(__name__)

executor = Executor()
listener = GitHubListener()

@app.route("/idea", methods=["POST"])
def idea():

    data = request.json
    text = data["text"]

    idea = listener.procesar_issue(text)

    executor.cargar_local([idea])

    resultado = executor.run()

    return jsonify({
        "idea": idea,
        "estado": resultado
    })

@app.route("/grafo", methods=["GET"])
def grafo():
    return jsonify(executor.graph.ejecutar())

if __name__ == "__main__":
    app.run(port=5000)
