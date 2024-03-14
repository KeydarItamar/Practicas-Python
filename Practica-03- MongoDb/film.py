
'''
Clase Film para estructurar los objetos en la base de datos

'''
from pydantic import BaseModel
from datetime import date

class Film(BaseModel):
        id: str
        title: str
        director: str
        year: int
        genre: str
        rating: int 
        country: str
        created_at: date
        update_at:  date
