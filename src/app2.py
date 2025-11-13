form flsk import 

from config import config


app = Flak (__name__)

conexion=MySQL(app)

@app.route('/alumnos', methods['GET'])
def listar_alumnos():
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT matricula, nombre, apaterno, amaterno, correo FROM alumnos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos=[]
        for fila in datos:
            alumno={'matricula':fila[0], 'nombre':fila[1], 'apellido':fila[2],
                'correo':fila[3]}
            alumnos.append(alumno)
        return jsonify({'alumnos':alumnos,'mensaje':'Alumnos encontrados',
                        "exito":True})
    except Exeption as ex:
        return jsonify({'mensaje':'Error al listar alumnos:{}'+str(ex),
                        "exito":False})

def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()