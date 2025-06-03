from flask import Flask

app = Flask(__name__)

#Criação da rota com um endpoint
@app.route("/")
def hello_wolrd():
    return "Hello World"

@app.route("/recurso")
def meu_recurso():
    return "<h1> Meu recurso no ar </h1>"


#se o app for executado diretamente inicia a aplicação flask
if __name__ == "__main__":
    app.run(debug=True)