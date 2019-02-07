import web 
import config as config 

class Delete: 
    def __init__(self):
        pass

    def GET(self, nombre_cli):
        clientes = config.model_clientes.select_nombre_cli(nombre_cli) #selecciona el registro que coincida con nombre
        return config.render.delete(clientes) #envia el resgistro y renderiza delete.html

    def POST(self, nombre_cli):
        formulario = web.input() #crea un objeto formulario con los datos enviados con el formulario 
        nombre_cli = formulario['nombre_cli'] #obtiene el nombre almacenado en el formulario
        config.model_clientes.delete_clientes(nombre_cli) #borra el registro del nombre seleccionado
        raise web.seeother('/clientes') #renderiza a raiz
        