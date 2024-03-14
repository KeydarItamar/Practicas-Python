
def schema_product(data)->dict:
    return { "product_id": str(data['_id']),
              "name": data[1],
              "description" : data[2],
              "company":data[3],
              "price": data[4],
              "units": data[5],
              "subcategory_id": data[6]
            }
    
    
def products_schema(data)-> dict:
    return[schema_product(prod) for prod in data]
  
  
def schema_Allproduct(data)->dict:
    return { "category_name": data[0],
              "subcategory_name" : data[1],
              "product_name":data[2],
              "product_brand": data[3],
            }
    
def products_Allschema(data)-> dict:
    return[schema_Allproduct(prod) for prod in data]   

  
