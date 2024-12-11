from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from jproperties import Properties
import requests



app = Flask(__name__)

@app.route('/api/v1/Python-test/count-files', methods=['POST', 'GET', 'PUT', 'DELETE'])
def count_files():
    if request.method == 'GET':
        directorio = os.getcwd()
        archivos = list(filter(os.path.isfile, os.listdir(directorio)))
        for archivo in archivos:
            print (archivo)
        if archivo: 
            for archivo in archivos:

                json ={
                    'name' : archivos,
                } 
                
            return jsonify(json)
        else:
            return jsonify({'error': 'No hemos podido encontrar los archivos.'}), 401
            
@app.route('/api/v1/Python-test/propeties', methods=['POST', 'GET'])
def properties():
        p = Properties()
        titulo = input("titulo de la propiedad:")
        contenido = input("contenido de la propiedad:")
        p[titulo] = contenido
        with open("application.properties", "wb") as f:
            p.store(f, encoding="utf-8")
        return jsonify({'campo actualizado con exito'}),500

            
@app.route('/api/v1/Python-test/delete', methods=['POST', 'GET', 'DELETE'])
def delete():
    x = requests.delete('/api/v1/Python-test/')
    # p = Properties()
    # titulo = input("titulo de la propiedad:")
    # contenido = input("contenido de la propiedad:")
    # p[titulo] = contenido
    # with open("application.properties", "wb") as f:
    #     p.store(f, encoding="utf-8")
    return jsonify({'campo actualizado con exito'}),500
                

if __name__ == '__main__':
    app.run(debug=True, port=8000)

    
