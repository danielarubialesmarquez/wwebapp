import web 
import config as config

class Index:
    def __init__(self):
        pass

    def GET(self):
        return config.render.index() #Envia todos los registros y renderiza index.html