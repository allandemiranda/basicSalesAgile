from app import app, db

@app.route("/")
def index():
    return "Olá Mundo"
