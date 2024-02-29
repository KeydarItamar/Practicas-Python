#Script de configuracion de la base de datos y metodos para el crud
from clientdb import *
from readfile import *

#funcion para devolver casi todos los elementos de la tabla
def findAlldata():
    cursor = client()
    try:
        cursor.execute("""
                        SELECT 
                            c.name AS category_name,
                            s.name AS subcategory_name,
                            p.name AS product_name,
                            p.company AS product_brand,
                            p.price AS product_price
                        FROM 
                            product p
                        JOIN 
                            subcategory s ON p.subcategory_id = s.subcategory_id
                        JOIN 
                            category c ON s.category_id = c.category_id;""")
        
        data =cursor.fetchall()
        print(data)
    except Exception as e:
        print(f'error: {e}')
    finally:
        cursor.close()
        return data
        
  

# Funcion para encontrar todos los elementos de una tabla
def findAll():
    cursor = client()
    cursor.execute(f'SELECT * FROM product')
    data = cursor.fetchall()
    return data

# Funcion para encontrar un elemento por Id 
def findbyId(Id):
    cursor = client()
    cursor.execute(f'SELECT * FROM product where product_id= {Id}')
    data = cursor.fetchone()
    return data


# Hacer un Insert en la tabla Product
def insertProduct(product_id, name, description, company, price, units, subcategory_id):
    cursor = client()
    try:
        cursor.execute(f"""INSERT INTO product (product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) \
                        VALUES({product_id}, '{name}', '{description}', '{company}', {price}, {units}, {subcategory_id}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP); 
                       """)
        conn.commit() 
        print('Se ha insertado correctamente')
    except Exception as e:
        print('Error : ', e)    
        conn.rollback()
    finally:
        cursor.close()

# Editar un producto de la tabla product
def editProducte(id, product_id, name, description, company, price, units, subcategory_id):
    cursor = client()
    try:
       cursor.execute(f"""
                      UPDATE public.product
	                  SET product_id={product_id}, name='{name}', description='{description}', company='{company}', price={price}, units={units},
                                     subcategory_id={subcategory_id}, created_at=CURRENT_TIMESTAMP, updated_at=CURRENT_TIMESTAMP
	                  WHERE product_id= {id};
                      """)
                      
       conn.commit() 
       print('Se ha actualizado correctamente')
       
    except Exception as e:
        print('Error : ', e)    
        conn.rollback()
    finally:
        cursor.close()
        
# funcion para borrar un producto segun su Id 
def deleteById(Id):
   cursor = client() 
   try: 
       cursor.execute(f'Delete from product where product_id= {Id}')
       conn.commit() 

   except Exception as e: 
       print(f'Error: {e}')
       conn.rollback()
   finally:
        cursor.close()        


# Funcion para crear una tabla 
def create_table(table):
    cursor = client()
    try:
        cursor.execute(table)
        conn.commit()  
        print(f'Tabla {table} creada correctamente')
    except Exception as e:
      print('Error : ', e)    
      conn.rollback()
    finally:
      cursor.close()

# Querys dadas en clase para crear las tablas  
tabla_category = """CREATE TABLE category (
                    category_id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP
                );"""

tabla_subcategory="""CREATE TABLE subcategory (
                    subcategory_id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    category_id INT NOT NULL,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP,
                    FOREIGN KEY (category_id) REFERENCES category(category_id)
                );"""

tabla_product= """CREATE TABLE product (
                    product_id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    company VARCHAR(255) NOT NULL,
                    price DECIMAL(10,2) NOT NULL,
                    units NUMERIC,
                    subcategory_id INT NOT NULL,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP,
                    FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)
                );"""
                
                
                
                
#Meter datos en las tablas
def insertCategory():
    cursor = client()
    lista = loadCategory('llista_productes.csv')
    try:
        for value in lista:
            id_categoria=value['id_categoria']
            nom_categoria=value['nom_categoria']
            
            sqlexiste = (f"""SELECT * FROM category where category_id = {id_categoria}""")
            sqlInsert= (f"""INSERT INTO category( category_id, name, created_at, updated_at)
                    VALUES ({id_categoria}, '{nom_categoria}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);""")
            cursor.execute(sqlexiste)
            existe = cursor.fetchone()
            if not existe:   
                cursor.execute(sqlInsert)

    except Exception as e:
      print('Error : ', e)    
      conn.rollback()
    finally:
      conn.commit()
      cursor.close()

def insertSubCategory():
    cursor = client()
    lista = loadsubCategory('llista_productes.csv')
    try:
        for value in lista:
            id_categoria=value['id_categoria']
            id_subcategoria=value['id_subcategory']
            nom_subcategoria= value['nom_categoria']
            
            sqlexiste = (f"""SELECT * FROM subcategory where subcategory_id = {id_subcategoria}""")
            
            sqlInsert= (f"""INSERT INTO subcategory(
	                        subcategory_id, name, category_id, created_at, updated_at)
	                        VALUES ({id_subcategoria}, '{nom_subcategoria}', {id_categoria}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);""")
            cursor.execute(sqlexiste)
            existe = cursor.fetchone()
            if not existe:   
                cursor.execute(sqlInsert)

    except Exception as e:
      print('Error : ', e)    
      conn.rollback()
    finally:
      conn.commit()
      cursor.close()
    

def insertCsvProduct():
    cursor = client()
    lista = loadproduct('llista_productes.csv')
    try:
        for value in lista:
            id = value["product_id"]
            nom = value['name']
            descrp = value["description"]
            comp = value["company"]
            precio= value["price"]
            unid = value["units"]
            id_sub = value["sub_id"]
            sqlexiste = (f"""SELECT * FROM product where product_id = {id}""")  
            sqlInsert= (f"""INSERT INTO product(
	                        product_id, name, description, company, price, units, subcategory_id, created_at, updated_at)
	                        VALUES ({id}, '{nom}', '{descrp}', '{comp}', {precio}, {unid}, {id_sub}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);""")
            
            cursor.execute(sqlexiste)
            existe = cursor.fetchone()
           
            if not existe:   
                cursor.execute(sqlInsert)

    except Exception as e:
      print('Error : ', e)    
      conn.rollback()
    finally:
      conn.commit()
      cursor.close()
    
# insertCsvProduct()    
# insertCategory()
# insertSubCategory()
# create_table(tabla_category)   llamos a la funcion una sola vez.
# create_table(tabla_subcategory)   llamos a la funcion una sola vez.
# create_table(tabla_product)  llamos a la funcion una sola vez.