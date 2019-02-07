import web 
import config as config 

class Uppdate:
    def __init__(self):
        pass
    
    def GET(self, id_pro):
        productos =config.model_productos.select_id_pro(id_pro) #selecciona el registro que coincida con nombre
        return config.render.update(productos) #envia el registro update.html

    def POST(self, nom_p):
        formulario = web.input() #almacena los datos del formulario web
        id_pro = formulario['id_pro'] #almacena el nombre de input email
        nom_p = formulario['nom_p']
        cantidad = formulario['cantidad']
        fecha = formulario['fecha']
        precio = formulario['precio']

        config.model_productos.update_productos(id_pro,nom_p,cantidad,fecha,precio) #actualiza los valores
        raise web.seeother('/productos') #redirecciona el index