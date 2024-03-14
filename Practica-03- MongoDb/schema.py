
def schema_film(data)->dict:
    return { 
            "_id":  str(data['_id']),
            "title": data['title'],
            "director": data['director'],
            "year": data['year'],
            "genre":  data['genre'],
            "rating":  data['rating'],    
            "country":  data['country'],
            }

def films_schema(data)-> dict:
    return[schema_film(film) for film in data]
  
  
def schema_Allproduct(data)->dict:
    return { "category_name": data[0],
              "subcategory_name" : data[1],
              "product_name":data[2],
              "product_brand": data[3],
            }
    
def products_Allschema(data)-> dict:
    return[schema_Allproduct(prod) for prod in data]   


