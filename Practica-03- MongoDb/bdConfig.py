
'''
Ejercicio de MongodB y Fast api hecho por Itamar Keydar 
DAW2B 14/03/2024

En este archivo estan todas las funciones donde manejamos la base datos

'''

import pymongo
import json
from  schema import *
from client import *
from bson import ObjectId

mycol = cliente()

#Cargamos toda la informacion falsa del archivo Json
with open('fakedata.json', 'r') as archivo:
    datos_json = archivo.read()
    datos = json.loads(datos_json)

#Funcion para insertar un objeto Film en la base de datos
def inserOne(film):
    mycol = cliente()
    mycol.insert_one(film)
    return 'Insert correctamente'
    
#Funcion para llenar la base de datos de informacion
def insertAlldata(data):
    for film in data:
        x = mycol.insert_one(film)
       
#Funcion para encontrar todos los elementos de la base de datos  
def findAll():
    mycol = cliente()
    data= []
    for x in mycol.find():
         data.append(x)
    return data   

#Funcion para encontrar un elemento con un id determinado
def findById(id):
    mycol = cliente()
    for x in mycol.find( { "_id": id }):
        if x is not None:
            return x
        else:
            'error'

#Funcion para para actualizar los datos de un elemento seleccionado a partir de un id
def updateFilm(film, id):
    mycol = cliente() 
    try:
        result = mycol.update_one({"_id": str(id)}, {"$set": film})
        if result.modified_count > 0:
            return 'Actualización realizada correctamente'
        else:
            return 'No se encontró ningún documento para actualizar'
    except Exception as e:
        return f'Error durante la actualización: {str(e)}'
    

#Funcion para borrar un elemento de la base de datos con determinado id
def deleteFilm(id):
    mycol = cliente()  
    try:
        result = mycol.delete_one({"_id": str(id)})
        if result.deleted_count > 0:
            return 'Delete realizadp correctamente'
        else:
            return 'No se encontró ningún documento para borrar'
    except Exception as e:
        return f'Error durante la actualización: {str(e)}'


#Funcion para encontrar todas las peliculas de un genero especifico
def findAllGenre(genre):
    mycol = cliente()
    data= []
    if genre is None or genre not in ["Action", "Drama", "Romance", "Thriller", "Comedy", "Horror", "Documentary", "Animation"]:
        return f'error Género inválido'
    for x in mycol.find({"genre": genre}):
         data.append(x)
         print(len(data))
    if not data:
        return 'No hay peliculas de este genero'
    return data  


#Funcion para encontrar todos las peliculas que tengan un "field" determinado y ordenarlos
def findAllOrder(field, order ):
    if order == 'asc': order = 1 
    else: order = -1
    
    mycol = cliente()
    data= []
    for x in mycol.find().sort(field, order):
         data.append(x)

    return data  

#Funcion que devuelve una cantidad especifica de elementos films
def findLimit(limit ):
    mycol = cliente()
    data= []
    for x in mycol.find().limit(limit):
         data.append(x)

    return data  


#Funcion que llamamos una vez para insertar todos los datos del Json
# insertAlldata(datos)
