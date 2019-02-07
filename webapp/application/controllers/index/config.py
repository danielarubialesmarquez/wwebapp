import web #Importa la libreria web.py
import application.models.model_index as model_index #Importa el modelo_clientes

render = web.template.render('application/views/index/', base='master') #configura la ubicacion de las vistas
