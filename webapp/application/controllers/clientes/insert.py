import web 
import config as config

class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert() #renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() #almacena los datos del formulario
        nombre_cli = formulario['nombre_cli'] #almacena el nombre escrito en el input
        ape_pa = formulario['ape_pa']
        ape_ma = formulario['ape_ma']
        empresa = formulario['empresa']
        email = formulario['email']

        config.model_clientes.insert_clientes(nombre_cli,ape_pa,ape_ma,empresa,email) #llama al metodo insert_datos y le pasa los datos guardados
        raise web.seeother('/clientes') #redirecciona al index.html
