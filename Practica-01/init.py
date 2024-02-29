import psycopg2

conn= psycopg2.connect(
            database= "postgres",
            user= "user_postgres",
            password= "pass_postgres",
            host= 'localhost',
            port= 5432
            )
                        
cursor= conn.cursor()

try:
    print(conn)

   
    #cursor.execute("INSERT INTO TEST (id, nom, edat, text) VALUES (13, 'LUIs', 35, 'todopoderoso');")
    
    conn.commit()  
    cursor.execute('SELECT * FROM TEST')
    
    datos= cursor.fetchall()
    for dato in datos:
        print(dato)
        
except Exception as e:
      print('Error : ', e)    
      conn.rollback()
        
finally:
    conn.close()
    cursor.close()