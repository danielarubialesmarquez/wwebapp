import web #Importa la libreria web.py
import application.models.model_clientes as model_clientes #Importa el modelo_clientes

render = web.template.render('application/views/clientes/', base='master') #configura la ubicacion de las vistas
