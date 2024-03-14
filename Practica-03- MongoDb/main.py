
'''
Ejercicio de MongodB y Fast api hecho por Itamar Keydar 
DAW2B 14/03/2024

En este archivo estan las rutas de Fast Api

'''
from typing import Union
from fastapi import FastAPI
import json
from decimal import Decimal
from datetime import datetime  
from film import *
from bdConfig import *
from  schema import *
import client

app = FastAPI()

#ruta inicial con saludo
@app.get("/")
def HelloOriol():
    return 'Hello Oriol'

#ruta que devuelve todas las peliculas
@app.get("/films")
def getFilms():
    try:
        data= findAll()
        data_json = films_schema(data)
        return data_json
    
    except Exception as e:
        print(f'Error: {e}')
        
#ruta que devuelve la pelicula con el id seleccionado
@app.get("/filmId/{id}")
def getFilmsId(id: str):
    try:
        data = findById(id) 
        data_json = schema_film(data) #Transformamos en json
        return data_json
    except Exception as e:
        print(f'Error: {e}')

#ruta para introducir una pelicula en la base de datos       
@app.post("/films")
def postFilms(film: Film):
    dict_film={ 
            "_id": (film.id),
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre":  film.genre,
            "rating":  film.rating,    
            "country":  film.country,
            }
    try:
        return inserOne(dict_film)
    
    except Exception as e:
        print(f'Error: {e}')
        
#Ruta que permita cambiar los datos de la pelicula seleccionada por id
@app.put("/filmsUpdate/{id}")
def putFilms(film: Film, id: str):
    dict_film={ 
        "_id": film.id,
        "title": film.title,
        "director": film.director,
        "year": film.year,
        "genre":  film.genre,
        "rating":  film.rating,    
        "country":  film.country,
        }
    try:
        return updateFilm(dict_film, id)
    
    except Exception as e:
        print(f'Error: {e}')

#Ruta para eleminar una pelicula de la base de datos
@app.delete("/films/{id}")
def deleteFilms(id:str):
    try:
        return deleteFilm(id)
    
    except Exception as e:
        print(f'Error: {e}')
        
#Ruta para encontrar todas las peliculas del genero seleccionado
@app.get("/filmsGenre/{genre}")
def getFilmsGenre(genre):
    try:
        data= findAllGenre(genre)
        data_json = films_schema(data)
        return data_json
    
    except Exception as e:
        return ({'error': 'Ha ocurrido un error al obtener las películas del género especificado'})
            
#Ruta que devuelve todas las peliculas con el campo seleccionado y en el orden especifico
@app.get("/filmsOrdered/{field}/{order}")
def getFilmsGenre(field, order):
    try:
        data= findAllOrder(field, order)
        data_json = films_schema(data)
        return data_json
    
    except Exception as e:
        return ({'error': 'Ha ocurrido un error al obtener las películas del género especificado'})

#ruta que devuelve un numero de peliculas seleccionado
@app.get("/filmsLimit/{limit}")
def getFilmsGenre(limit: int):
    try:
        data= findLimit(limit)
        data_json = films_schema(data)
        return data_json
    
    except Exception as e:
        return ({'error': 'Ha ocurrido un error al obtener las películas del género especificado'})