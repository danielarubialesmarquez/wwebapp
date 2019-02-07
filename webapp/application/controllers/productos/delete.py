import web 
import config as config 

class Deletee: 
    def __init__(self):
        pass

    def GET(self, id_pro):
        productos = config.model_productos.select_id_pro(id_pro) #selecciona el registro que coincida con nombre
        return config.render.delete(productos) #envia el resgistro y renderiza delete.html

    def POST(self, id_pro):
        formulario = web.input() #crea un objeto formulario con los datos enviados con el formulario 
        id_pro = formulario['id_pro'] #obtiene el nombre almacenado en el formulario
        config.model_productos.delete_productos(id_pro) #borra el registro del nombre seleccionado
        raise web.seeother('/productos') #renderiza a raiz
        