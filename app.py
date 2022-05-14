from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Olá, eu sou o Braz. Sou líder de QA. Segue meu Linkedin: https://www.linkedin.com/in/felipe-braz/"

if __name__ == '__main__':
    app.run()