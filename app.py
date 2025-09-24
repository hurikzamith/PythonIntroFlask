from flask import Flask

app = Flask(__name__)

# Rota raíz
@app.route('/')
def hello_world():
    return 'Hello World'

# Modo para desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)