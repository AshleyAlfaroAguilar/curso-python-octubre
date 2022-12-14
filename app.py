from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hola mundo"

@app.route('/saludar/<nombre>')
def saludar (nombre):
    return f"Muchos saludos {nombre}"

@app.route("/verificar-edad/<int:edad>")
def verificar_edad(edad):
    return f'tienes {edad} años'

@app.route('/users', methods=['POST'])
def store_user():
    return "se guardo el usuario"

@app.post('/address')
def store_address():
    return "Direccion guardada"

@app.put('/users')
def update_user():
    return {
        'name': request.form['name'],
        'age': request.form['age'],
        'method': request.method
    }

@app.get('/users')
def List_Users():
    return [
        {
            'name': "jorge",
            'apellido': "Gonzalez",
            'edad':34
        }
    ]

@app.errorhandler(404)
def not_found(error):
    return "ups,esta pagina no existe"
