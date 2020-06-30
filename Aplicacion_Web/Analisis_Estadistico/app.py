# DEPENDENCIAS:
# FLASK
# FLASK_MYSQL

from flask import Flask, render_template, request
from flaskext.mysql import MySQL


app = Flask(__name__)

# CONEXION DB


@app.route('/login')
def index():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    texto = "Cuenca"
    return render_template("dashboard.html", texto=texto)


if __name__ == '__main__':
    app.run(debug=True)
