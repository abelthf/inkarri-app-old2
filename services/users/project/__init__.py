from flask import Flask, jsonify

# instanciamos la app
app = Flask(__name__)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'estado': 'satisfactorio',
        'mensaje': 'pong!!!'
    })