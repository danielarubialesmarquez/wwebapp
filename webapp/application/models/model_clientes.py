import config as config #Importa el archivo config
db = config.DB #crea un objeto db creado en config
"""
Metodo para selecionar todos los registros dela tabla
"""
def select_clientes():
    try:
        return db.select('clientes') #selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_clientes Error {}",format(e.args) #
        print "Model select_clientes Message {}",format(e.message) #
        return None
"""
Metodo para selecionar un registro que coincida con el nombre dado
"""
def select_nombre_cli(nombre_cli):
    try:
        return db.select('clientes',where='nombre_cli=$nombre_cli', vars =locals())[0] #seleciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre_cli Error {}",format(e.args) #
        print "Model select_nombre_cli Message {}",format(e.message) #
        return None    
"""
Metodo para insertar un nuevo registro usando nombre y email
"""
def insert_clientes(nombre_cli, ape_pa, ape_ma, empresa, email): #persona
    try:
        return db.insert('clientes', nombre_cli=nombre_cli, ape_pa=ape_pa, ape_ma=ape_ma, empresa=empresa, email=email) #inserta un registro en personas
    except Exception as e:
        print "Model insert_clientes Error {}",format(e.args)
        print "Model insert_clientes Message {}",format(e.message)
        return None
"""
Metodo para selecionar todos los registros dela tabla
"""
def delete_clientes(nombre_cli): #persona
    try:
        return db.delete('clientes', where='nombre_cli=$nombre_cli', vars=locals()) #borra un registro de una persona
    except Exception as e:
        print "Model delate_clientes Error {}",format(e.args)
        print "Model delate_clientes Message {}",format(e.message)
        return None
"""
Metodo para actualizar el email, del nombre recibido
"""
def update_clientes(nombre_cli, ape_pa, ape_ma, empresa, email): #actualiza el email de personas que coinciden con el nombre
    try:
        return db.update('clientes',
            ape_pa=ape_pa,
            ape_ma=ape_ma,
            empresa=empresa,
            email=email,
            where='nombre_cli=$nombre_cli',
            vars=locals())
    except Exception as e:
        print "Model update_clientes Error {}",format(e.args)
        print "Model update_clientes Message {}",format(e.message)
        return None
