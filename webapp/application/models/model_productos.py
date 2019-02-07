import config as config #Importa el archivo config
db = config.DB #crea un objeto db creado en config
"""
Metodo para selecionar todos los registros dela tabla
"""
def select_productos():
    try:
        return db.select('productos') #selecciona todos los registros de la tabla personas
    except Exception as e:
        print "Model select_productos Error {}",format(e.args) #
        print "Model select_productos Message {}",format(e.message) #
        return None
"""
Metodo para selecionar un registro que coincida con el id dado
"""
def select_id_pro(id_pro):
    try:
        return db.select('productos',where='id_pro=$id_pro', vars =locals())[0] #seleciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_id_pro Error {}",format(e.args) #
        print "Model select_id_pro Message {}",format(e.message) #
        return None    
"""
Metodo para insertar un nuevo registro
"""
def insert_productos(id_pro, nom_p, cantidad, fecha, precio): #persona
    try:
        return db.insert('productos', id_pro=id_pro, nom_p=nom_p, cantidad=cantidad, fecha=fecha, precio=precio) #inserta un registro en personas
    except Exception as e:
        print "Model insert_productos Error {}",format(e.args)
        print "Model insert_productos Message {}",format(e.message)
        return None
"""
Metodo para selecionar todos los registros dela tabla
"""
def delete_productos(id_pro): #persona
    try:
        return db.delete('productos', where='id_pro=$id_pro', vars=locals()) #borra un registro de una persona
    except Exception as e:
        print "Model delate_productos Error {}",format(e.args)
        print "Model delate_productos Message {}",format(e.message)
        return None
"""
Metodo para actualizar 
"""
def update_productos(id_pro, nom_p, cantidad, fecha, precio): #actualiza el email de personas que coinciden con el nombre
    try:
        return db.update('productos',
            nom_p=nom_p,
            cantidad=cantidad,
            fecha=fecha,
            precio=precio,
            where='id_pro=$id_pro',
            vars=locals())

    except Exception as e:
        print "Model update_productos Error {}",format(e.args)
        print "Model update_productos Message {}",format(e.message)
        return None
