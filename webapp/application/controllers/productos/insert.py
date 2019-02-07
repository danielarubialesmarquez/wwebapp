import web 
import config as config

class Inserttt:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert() #renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        id_pro = formulario['id_pro'] #almacena el nombre escrito en el input
        nom_p = formulario['nom_p']
        cantidad = formulario['cantidad']
        fecha = formulario['fecha']
        precio = formulario['precio']

        config.model_productos.insert_productos(id_pro,nom_p,cantidad,fecha,precio) #llama al metodo insert_datos y le pasa los datos guardados
        raise web.seeother('/productos') #redirecciona al index.html
