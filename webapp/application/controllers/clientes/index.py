import web 
import config as config

class Index:
    def __init__(self):
        pass

    def GET(self):
        clientes = config.model_clientes.select_clientes().list() #selecciona todos los registros de personas
        return config.render.index(clientes) #Envia todos los registros y renderiza index.html