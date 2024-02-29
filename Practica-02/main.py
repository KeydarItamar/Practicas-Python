from typing import Union
from fastapi import FastAPI
from product_db_config import *
from Product import *
import json
from decimal import Decimal
from datetime import datetime  
from schema import *
 
             
app = FastAPI()

@app.get("/productAll")
def getAllProducts():
    try:
        data= findAlldata()
        jsondata = products_Allschema(data)
        return jsondata
    
    except Exception as e:
        print(f'Error: {e}')

# ruta que devuelve todos los productos de la tabla product 
@app.get("/product")
def getProducts():
    try:
        data= findAll()
        jsondata = products_schema(data)
        return jsondata
    
    except Exception as e:
        print(f'Error: {e}')
        
# ruta que devuelve un producto en funcion de su Id
@app.get("/product/{id}")
def getProduct_Id(id:int):
    try:
        data= findbyId(id)
        jsondata= schema_product(data)
        return jsondata
    except Exception as e: 
        print(f'Error: {e}')
        
# ruta que permite introducir un producto en la base de datos
@app.post("/product")
def addProduct(prod: Product):
    try: 
      insertProduct(prod.product_id, prod.name, prod.description, prod.company, prod.price, prod.units, prod.subcategory_id)
      print('Se ha insertado correctamente')
    except Exception as e:
        print('No se ha podido insertar correctamente')
        print(f'Error: {e}')
        
        
# ruta que permite editar un producto de la tabla 
@app.put("/product/{id}")
def editProduct(prod: Product, id: int):
    time= date
    try:
        editProducte( id, prod.product_id, prod.name, prod.description,
                            prod.company,prod.price,prod.units, prod.subcategory_id,
                            )
        
        print('Se ha editado correctamente')
        return getProduct_Id(id)

    except Exception as e:
        print('No se ha podido edirtar el producto')
        print(f'Error : {e}')
        
# Ruta parra borrar un producto de la tabla segun su id

@app.delete("/product/{id}")
def delete(id: int):
    try:
        deleteById(id)
        print('Se ha borrado correctamente')
    except Exception as e:
        print('No se ha podido borrar el producto')
        print(f'Error : {e}') 
           
@app.get("/productAll")
def getProductsAll():
    return findAll('product')    
    
