def suma(a, b):
    return a+b 

def mostra_num():
    num1=int(input('Introduce un numero: '))
    num2=int(input('Introduce un numero: '))
    if num1 < num2:
        num1, num2 = num2, num1

    suma_total = 0            
    for i in range(num2, num1 +1):
        print(i)
        suma_total+=i
    print(f'la suma total de los numeros es: {suma_total}')

def nom():
    nom= input('Introduce tu nombre: ')
    print(f'Hola {nom}')