import modules.webscrapingFilmmaffinity as Filmaffinity
import modules.APIthemoviedb as APImovie
import modules.APIyoutube as APIyoutube
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    # Obtener los datos del formulario
    termino_busqueda = request.form.get('termino_busqueda')
    api_key = "0cf8bcf44c54573b1364140cd12ac30f"
    # Ejecutar el script de Python y obtener los resultados
    if(termino_busqueda == "" ):
        return render_template('error.html')
    else:
        item1 = Filmaffinity.buscar_pelicula_filmaffinity(termino_busqueda)
        
        item2 = APImovie.obtener_informacion_pelicula(termino_busqueda, api_key)
        
        item3= APIyoutube.obtener_trailer(termino_busqueda)
        #Pasar los resultados a la plantilla resultado.html
        resultado=[item1,item2,item3]
        return render_template('resultado.html',resultado=resultado)

@app.route("/volver")
def volver():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
