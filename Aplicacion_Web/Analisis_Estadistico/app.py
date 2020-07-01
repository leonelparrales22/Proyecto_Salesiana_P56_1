# DEPENDENCIAS:
# FLASK
# FLASK_MYSQL
from flask import Flask, render_template, request, redirect, url_for, json, jsonify
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
colores = ["#75389b", "#2c63e2", "#e90504", "#fed10c", "#00a728", "#ff9a00"]


def comprobar_usuario(cedula_usuario, contrasenia):
    cursor.execute(
        f'SELECT * FROM `USUARIOS` WHERE rol="ADMIN" AND cedula_usuario="{cedula_usuario}" AND contrasenia="{contrasenia}"')
    data = cursor.fetchone()
    return data


def marca_celular_mas_vendido():
    cursor.execute(
        'SELECT CELULARES.marca_celular, COUNT(CELULARES.marca_celular) AS PROMEDIO FROM `DETALLE_VENTA`,`CELULARES` '
        'WHERE DETALLE_VENTA.id_celular = CELULARES.id_celular GROUP BY CELULARES.marca_celular')
    data = cursor.fetchall()
    total = 0
    contador = -1
    grafico = "["
    for x in data:
        total += x[1]
        contador += 1
    contador = 1
    for x, color in zip(data, colores):
        lista = {
            "label": x[0],
            "data": x[1] / total,
            "color": color
        }
        y = json.dumps(lista)
        grafico += y
        if len(data) != contador:
            grafico += ","
        contador += contador
    grafico += "]"
    return grafico


def calcular_rango_celulares_mas_vendido():
    cursor.execute(
        'SELECT CELULARES.precio_celular FROM `DETALLE_VENTA`, `CELULARES` WHERE DETALLE_VENTA.id_celular = '
        'CELULARES.id_celular')
    data = cursor.fetchall()
    contador_menos_100 = 0
    contador_entre_100_200 = 0
    contador_entre_200_300 = 0
    contador_entre_300_400 = 0
    contador_entre_400_500 = 0
    contador_mayores_500 = 0
    total = -1
    for x in data:
        total += 1
        if x[0] <= 100:
            contador_menos_100 += 1
            continue
        if 100 < x[0] <= 200:
            contador_entre_100_200 += 1
            continue
        if 200 < x[0] <= 300:
            contador_entre_200_300 += 1
            continue
        if 300 < x[0] <= 400:
            contador_entre_300_400 += 1
            continue
        if 400 < x[0] <= 500:
            contador_entre_400_500 += 1
            continue
        if x[0] > 500:
            contador_mayores_500 += 1
            continue

    grafico = "["
    lista = {
        "label": "Menos de $100",
        "data": contador_menos_100 / total,
        "color": colores[0]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $100 y $200",
        "data": contador_entre_100_200 / total,
        "color": colores[1]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $200 y $300",
        "data": contador_entre_200_300 / total,
        "color": colores[2]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $300 y $400",
        "data": contador_entre_300_400 / total,
        "color": colores[3]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $400 y 500",
        "data": contador_entre_400_500 / total,
        "color": colores[4]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Mayores a 500",
        "data": contador_mayores_500 / total,
        "color": colores[5]
    }
    y = json.dumps(lista)
    grafico += y
    grafico += "]"
    return grafico


marca_celular_mas_vendido()
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
        return render_template("dashboard.html", texto=texto, g1=str(marca_celular_mas_vendido()),
                               g2=calcular_rango_celulares_mas_vendido())


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
