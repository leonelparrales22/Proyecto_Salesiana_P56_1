# DEPENDENCIAS:
# FLASK
# FLASK_MYSQL
from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)

# DATABASE CONFIG
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'bdd'
app.config['MYSQL_DATABASE_Host'] = 'localhost'
mysql.init_app(app)
# DATABSE CONNECTION
conn = mysql.connect()
cursor = conn.cursor()


# BDD MANAGE
def comprobar_usuario(cedula_usuario, contrasenia):
    cursor.execute(
        f'SELECT * FROM `USUARIOS` WHERE rol="ADMIN" AND cedula_usuario="{cedula_usuario}" AND contrasenia="{contrasenia}"')
    data = cursor.fetchone()
    return data


# WEB APLICATION
validar = False


@app.route('/', methods=['GET', 'POST'])
def index():
    global validar
    validar = False
    texto = "Cuenca"
    if request.method == "POST":
        usuario = request.form['cedula']
        password = request.form['password']
        data = comprobar_usuario(usuario, password)
        if data is None:
            return render_template("index.html", error="Con_error")
        else:
            validar = True
            return redirect(url_for('dashboard'))
    return render_template("index.html", error="Sin_error")


@app.route('/dashboard')
def dashboard():
    texto = "Cuenca"
    print(validar)
    if not validar:
        return redirect(url_for('.index'))
    else:
        return render_template("dashboard.html", texto=texto)


@app.route('/logout')
def logout():
    global validar
    validar = False
    return redirect(url_for('.index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)
