import pymongo


#Funcion que genera la conexion con la base de datos de Mongo
def cliente():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["dbPython"]
    mycol = mydb["films"]
    return mycol