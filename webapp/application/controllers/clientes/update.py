import web 
import config as config 

class Update:
    def __init__(self):
        pass
    
    def GET(self, nombre_cli):
        clientes =config.model_clientes.select_nombre_cli(nombre_cli) #selecciona el registro que coincida con nombre
        return config.render.update(clientes) #envia el registro update.html

    def POST(self, email):
        formulario = web.input() #almacena los datos del formulario web
        nombre_cli = formulario['nombre_cli'] #almacena el nombre de input email
        ape_pa = formulario['ape_pa']
        ape_ma = formulario['ape_ma']
        empresa = formulario['empresa']
        email = formulario['email'] #almacena el email del input password

        config.model_clientes.update_clientes(nombre_cli,ape_pa,ape_ma,empresa,email) #actualiza los valores
        raise web.seeother('/clientes') #redirecciona el index