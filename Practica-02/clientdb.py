import psycopg2

# configuracion para la base de datos
conn= psycopg2.connect(
                database= "postgres",
                user= "user_postgres",
                password= "pass_postgres",
                host= 'localhost',
                port= 5432
                )

def client():
    try:   
        cursor= conn.cursor()                     
        return cursor
    except Exception as e:
        print(f'Error: {e}')
    