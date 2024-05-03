from flask import Flask, render_template, request, redirect, url_for, flash, session
from db.DataBaseConteoBoleta import ConteoBotosDB
from datetime import datetime
from Model.Votos_lista_completa import Votos_lista_completa
from Model.Votos_personalizado import Votos_personalizado
from Model.Votos_blanco import Votos_blanco
from Model.Votos_nulos import Votos_nulos
from Model.Data_sheet import Data_sheet


app = Flask(__name__)
app.secret_key = 'mysecretkey'
db = ConteoBotosDB()


# -----------  HOME PAGE  -----------
@app.route('/')
def home():
    return render_template('home.html')


# -----------  LOAD DATA SHEET -----------
@app.route("/load_data")
def load_data():
    return render_template("load_data.html")


# -----------  SAVE FORM DATA SHEET -----------
@app.route('/guardar_datos', methods=['POST', 'GET'])
def guardar_datos():
    if request.method == 'POST':
        data_sheet = Data_sheet(departamento=request.form['departamento'],
                                circuito=request.form['circuito'],
                                mesa=request.form['mesa'],
                                electores=request.form['electores'],
                                boletas=request.form['boletas'],
                                diferencia=request.form['diferencia'])
        db.insertDataSheet(data_sheet=data_sheet)
        flash(' Datos cargados.', 'alertExito')
    return redirect(url_for('selection_voto'))




# -----------  SELECTION ROUTE  -----------
@app.route("/selection_route")
def selection_route():
    return render_template("selectionRoute.html")


# -----------  SELECTION VOTOS  -----------
@app.route("/selection_voto")
def selection_voto():
    return render_template("selectionVoto.html")



# -----------  DATA SHEET  -----------
@app.route("/data_sheet")
def data_sheet():
    data = db.getAllDataSheet()
    votos_nulos = db.getAllVotosNulos()
    votos_blanco = db.getAllVotosBlanco()
    current_date = datetime.now().strftime('%d de %B de %Y')
    return render_template('data_sheet.html', sheet=data, date=current_date, nulos=votos_nulos, blancos=votos_blanco)



# -----------  BORRAR VOTOS  -----------
@app.route("/borrar_votos")
def borrar_votos():
    db.deleteAllVotosCompleta()
    db.deleteAllVotosPersonalizo()
    db.deleteAllVotosNulos()
    db.deleteAllVotosBlanco()
    return redirect(url_for('home'))


# -----------  BORRAR DATOS PLANILLA  -----------
@app.route("/borrar_datos_planilla")
def borrar_datos_planilla():
    db.deleteAllDataSheet()
    return redirect(url_for('home'))




# -----------  BOLETAS  -----------
# -----------  VOTO LISTA COMPLETA  -----------
@app.route("/boleta_all_voto")
def boleta_all_voto():
    return render_template("boletaVotoListaCompleta.html")


# -----------  ENVÍO DE VOTOS  -----------
@app.route('/registerVotoBoleta1', methods=['POST', 'GET'])
def registerVotoBoleta1():
    if request.method == 'POST':
        boleta1 = Votos_lista_completa(
            boleta1=request.form.get("boleta1"), boleta2='0', boleta3='0')
        db.insertVotosBoleta1(boleta1=boleta1)
        flash(' Votos cargados.', 'alertExito')
    return redirect(url_for('selection_voto'))


@app.route('/registerVotoBoleta2', methods=['POST', 'GET'])
def registerVotoBoleta2():
    if request.method == 'POST':
        boleta2 = Votos_lista_completa(
            boleta1='0', boleta2=request.form.get("boleta2"), boleta3='0')
        db.insertVotosBoleta2(boleta2=boleta2)
        flash(' Votos cargados.', 'alertExito')
    return redirect(url_for('selection_voto'))


@app.route('/registerVotoBoleta3', methods=['POST', 'GET'])
def registerVotoBoleta3():
    if request.method == 'POST':
        boleta3 = Votos_lista_completa(
            boleta1='0', boleta2='0', boleta3=request.form.get("boleta3"))
        db.insertVotosBoleta3(boleta3=boleta3)
        flash(' Votos cargados.', 'alertExito')
    return redirect(url_for('selection_voto'))


# -----------  VOTO LISTA PERSONALIZADA  -----------
@app.route("/boletaPersonalizada")
def boletaPersonalizada():
    return render_template("votoPersonalizado.html")


@app.route('/registerVotoPersonalizado', methods=['POST', 'GET'])
def registerVotoPersonalizado():
    if request.method == 'POST':
        votos_personalizados = Votos_personalizado()

        votos_personalizados.intendente1 = request.form.get(
            'intendente1', default='0')
        votos_personalizados.intendente2 = request.form.get(
            'intendente2', default='0')
        votos_personalizados.intendente3 = request.form.get(
            'intendente3', default='0')
        votos_personalizados.concejal1 = request.form.get(
            'concejal1', default='0')
        votos_personalizados.concejal2 = request.form.get(
            'concejal2', default='0')
        votos_personalizados.concejal3 = request.form.get(
            'concejal3', default='0')

        db.insertVotosPersonalizados(votos_personalizados)
        flash(' Votos cargados.', 'alertExito')

        print("Intendente 1:", votos_personalizados.intendente1)
        print("Intendente 2:", votos_personalizados.intendente2)
        print("Intendente 3:", votos_personalizados.intendente3)
        print("Concejal 1:", votos_personalizados.concejal1)
        print("Concejal 2:", votos_personalizados.concejal2)
        print("Concejal 3:", votos_personalizados.concejal3)

    return redirect(url_for('selection_voto'))






# -----------  VOTOS NULOS  -----------
@app.route("/votos_nulos")
def votos_nulos():
    return render_template("votos_nulos.html")


@app.route('/registerVotosNulos', methods=['POST', 'GET'])
def registerVotosNulos():
    if request.method == 'POST':
        votos_nulos = Votos_nulos()

        votos_nulos.votos = request.form.get('votos', default='0')

        db.insertVotosNulos(votos_nulos)
        flash(' Votos cargados.', 'alertExito')
    return redirect(url_for('selection_voto'))





# -----------  VOTOS BLANCO  -----------
@app.route("/votos_blanco")
def votos_blanco():
    return render_template("votos_blanco.html")


@app.route('/registerVotosBlanco', methods=['POST', 'GET'])
def registerVotoBlanco():
    if request.method == 'POST':
        votos_blanco = Votos_blanco()

        votos_blanco.votos = request.form.get('votos', default='0')

        db.insertVotosBlanco(votos_blanco)
        flash(' Votos cargados.', 'alertExito')
    return redirect(url_for('selection_voto'))
















# ARREGLAR DETALLES
# @app.route('/totalVotosPersonalizados')
# def total_votos_personalizados():
#     total_votos_listaPersonalizada = db.obtenerTotalVotosPersonalizados()
#     return f"Total de votos personalizados: {total_votos_listaPersonalizada}"

# @app.route('/totalVotosListaCompleta')
# def total_votos_lista_completa():
#     total_votos_listaCompleta = db.obtenerTotalVotosListaCompleta()
#     return f"Total de votos lista completa: {total_votos_listaCompleta}"


# VOTO LISTA COMPLETA
@app.route('/cantidadVotosEmitidos')
def cantidad_votos_emitidos():
    total_votos_emitidos = db.obtenerCantidadVotosEmitidos()
    return f"Cantidad de votos emitidos: {total_votos_emitidos}"


@app.route('/boletaGanadora')
def boleta_ganadora():
    ganadora = db.obtenerBoletaGanadora()
    votos_impuestos = db.obtenerVotosGanadora()
    return f"Boleta ganadora: {ganadora}<br>Se impuso con {votos_impuestos} votos"


# VOTO LISTA PERSONALIZADA
@app.route('/boletaGanadoraPersonalizada')
def boleta_ganadora_personalizada():
    ganadora_personalizada = db.obtenerBoletaGanadoraPersonalizada()
    return f"Boleta ganadora personalizada: {ganadora_personalizada}"


@app.route('/votosGanadoraPersonalizada')
def votos_ganadora_personalizada():
    votos_impuestos_personalizados = db.obtenerVotosGanadoraPersonalizada()
    return f"Votos impuestos en la boleta ganadora personalizada: {votos_impuestos_personalizados}"


# GANADOR DEFINITIVO
# @app.route('/ganadorDefinitivo')
# def ganador_definitivo():
#     ganador = db.obtenerGanadorDefinitivo()
#     return f"Ganador definitivo: {ganador}"
@app.route('/ganadorFinal')
def ganador_final():
    ganador = db.obtenerGanadorFinal()
    votoListaCompleta = db.obtenerVotosImpuestosListaCompleta(ganador)
    votoListaPersonalizada = db.obtenerVotosImpuestosPersonalizada(ganador)
    return f"Ganador definitivo ----->: {ganador}<br>Obtuvo los siguientes votos<br>Votos lista completa: {votoListaCompleta}<br>Votos lista personalizada: {votoListaPersonalizada}"


# @app.route('/votosImpuestos')
# def votos_impuestos():
#     votos_impuestos = db.obtenerVotosImpuestos()
#     return f"Votos impuestos: {votos_impuestos}"


app.run(host='0.0.0.0', port=5004, debug=True)
