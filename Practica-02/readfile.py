import pandas as pd

def loadCategory(file):
    dadesCSV = pd.read_csv(file, header=0)
    categorylist = []
    for index, row in dadesCSV.iterrows():
        fila = row.to_dict()
        lista = getCategory(fila["id_categoria"], fila["nom_categoria"])
        categorylist.extend(lista)  
    return categorylist

def loadsubCategory(file):
    dadesCSV = pd.read_csv(file, header=0)
    subCategorylist = []
    for index, row in dadesCSV.iterrows():
        fila = row.to_dict()
        subCategorylist.append(getSubcategoria(fila["id_subcategoria"],fila['id_categoria'], fila["nom_subcategoria"]))
    return subCategorylist 

def loadproduct(file):
    dadesCSV = pd.read_csv(file, header=0)
    subCategorylist = []
    for index, row in dadesCSV.iterrows():
        fila = row.to_dict()
        subCategorylist.append(getproducto(fila["id_producto"], fila['nom_producto'], fila["descripcion_producto"], 
                                          fila["companyia"],fila["precio"], fila["unidades"],fila["id_subcategoria"] ))
    return subCategorylist 


#id_categoria,nom_categoria,id_subcategoria,nom_subcategoria,id_producto,nom_producto,
# descripcion_producto,companyia,precio,unidades


def getCategory(id, name):
    return [{'id_categoria': id, 'nom_categoria': name}]

def getSubcategoria(sub_id, id, name):
    return {'id_subcategory':sub_id, 'id_categoria': id, 'nom_categoria': name, }

def getproducto(product_id, name, description, company, price, units, sub_id):
    return { 'product_id': product_id, 'name': name, 'description': description, 'company':company, 'price': price, 
            'units': units, 'sub_id': sub_id}
    

# var =load('llista_productes.csv')
# for n in var:
#     print(n)