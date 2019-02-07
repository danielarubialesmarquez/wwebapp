import web
import config as config

class Vieww:
    def __init__(self):
        pass

    def GET(self, id_pro):
        productos = config.model_productos.select_id_pro(id_pro) #selecciona el registro que coincisa con nombre
        return config.render.view(productos) #Envia el registro y renderiza view.html 
