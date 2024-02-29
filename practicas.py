import random

#Ejercicio 1: 
print('Hello World')

#Ejercicio 2: 
def ejercicio2():
    num1 = int(input('Introduce el primer numero: \n' ))
    num2 = int(input('Introduce el segundo numero: \n' ))
    print(f'La suma de los numeros es: {num1+num2}')
# ejercicio2()

#Ejercicio 3: 
def ejercicio3():
    frase = input('Introduce una frase: \n')
    frase_2 = frase.replace(' ', '')
    print(f'Frase sin espacio: {frase_2}')
    
#ejercicio3()

#Ejercicio 4: 
def ejercicio4():
 for i in range(0,501):
     if i%2 != 0: 
         print(i)

#ejercicio4()

#Ejercicio 5:
def ejercicio5():
     num_eur = float(input('Introduce un numearo en €: '))
     iva_aplicat = int(input('Introduce el IVA a aplicar: '))
     iva_total = num_eur * (iva_aplicat / 100)
     print(f'Valor introducido: {num_eur}€') 
     print(f'IVA Introducido: {iva_total}%')
     print(f'Valor final: {num_eur - iva_total}')
#ejercicio5()

#Ejercicio 6:
def ejercicio6():
    palabra_1 = input('Introduce una palabra: \n')
    palabra_2 = input('Introduce una palabra: \n')
    print(f'Palabra 1 tiene: {len(palabra_1)} letras.')
    print(f'Palabra 2 tiene: {len(palabra_2)} letras.')
    print(f'La primera letra de {palabra_1} es : {palabra_1[0]}')
    print(f'La primera letra de {palabra_2} es : {palabra_1[0]}')
#ejercicio6()

#Ejercicio 7: 
def ejercicio7():
    palabra = input('Introduce una palabra o frase: \n')
    palabra_inver = palabra[::-1]
    if palabra == palabra_inver:
        print(f'La palabra/frase que has introducido es un palindromo!')
        print(palabra_inver)
    else:
        print(f'{palabra}: palabra que has introducido, no es un palindromo: {palabra_inver}') 
           
#ejercicio7()    

#Ejercicio 8:
def adivina_numero():
    numero_aleatorio = random.randint(1, 100) 
    intentos= 0
    while True:
        try:
            user_num = int(input('Introduce un numero para adivinar mi numero secreto!\n'))
        except ValueError:
            print("Error: Por favor, introduce un número válido.")
            continue

        if numero_aleatorio == user_num:
            print(f'Enhorabuena has adivinado el numero! Era el {numero_aleatorio}')
            print(f'Numero de intentos usados: {intentos}')
            break
        elif user_num > numero_aleatorio:    
            print("El numero que has introducido es MAYOR al mio")
            intentos+=1
        else:
            print('El numero introducido es MENOR al mio')
            intentos+=1

     
        print('*' * 100)
       
#adivina_numero()

#Ejercicio 9:
def ejercicio9():
    lista = [1,2,3,4]
    tupla= (4,3,2,1)
    num1= 'valor - 1'
    num2= 'valor - 2'
    num3= 'valor - 3'
    diccionario= {num1: 1, num2: 2, num3: 3}
    print(f'Esto es una lista: {lista}\nEsto es una tupla: {tupla}\nEsto es un diccionario: {diccionario}')
    print('Lista y tupla nos permiten almacenar datos, como variables, objetos y otras listas/tuplas.\nPero las listas son mutables y las tuplas no.')
    print('Los diccionarios funciona de forma similar pero almacenan valores duales en forma de Key y Value.')
    
#ejercicio9()

#Ejercicio 10
def ejercicio10():
    meses_del_anio = ('enero', 'febrero', 'marzo',
                      'abril', 'mayo', 'junio', 'julio',
                      'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
     
    print(f'Estos son los meses del año : {meses_del_anio}')
    num = int(input('Introduce un numero de 0 a 11 para escoger mes: \n'))
    print(f'El mes escogido es: {meses_del_anio[num]}')

#ejercicio10()

# Ejercicio 11:
def ejercicio11():
    nums_frase = input('Introduce 10 números separados por espacios: ')

    numeros = [int(num) for num in nums_frase.split()]

    tupla_numeros = tuple(numeros)
    tupla_ordenada = tuple(sorted(tupla_numeros))

    print(f'Tupla ordenada: {tupla_ordenada}')
    
#ejercicio11()

# Ejercicio 12:
def ejercicio12():
    lista_w= []
    num= 1
    for i in range(10):
        word = input(f'Introduce la palabra numero {num}: ')
        num+=1
        lista_w.append(word)
    lista_ordenada = sorted(lista_w)
    print(f'La lista ordenada queda asi: {lista_ordenada}')    

#ejercicio12()

# Ejercicio 13:
def ejercicio13():
    lista_w= []
    word1= input('Introduce la primera palabra: \n')
    word2= input('Introduce la segunda palabra: \n')
    lista_w.append(word1)
    lista_w.append(word2)
    dic_a = {}    
    for word in lista_w:
        for letra in word:
            dic_a[letra] = dic_a.get(letra, 0) + 1
    print(f'Para las palabras = {word1} y {word} el calculo queda asi: \n {dic_a}')
    
#ejercicio13()

def ejercicio14():
    areas_pis = {'Menjador': 10.15, 'Rebedor': 9.56, 'Habitació1': 12.34,
                 'Terrassa': 15.55, 'Lavabo': 7.98, 'Cuina': 12, 'Habitació2': 12.2 }
        
    print(f'Imprimir el segon element: {areas_pis}')
    print(f'Imprimir lúltim element: {areas_pis[-1]}')
    print(f'Imprimir làrea de la terrassa: {areas_pis[3,1]}')
    print(f'Imprimir del primer element al tercer element')
    print(f'Imprimir del tercer element a lúltim')
    print(f'Imprimir el total de làrea de les dues habitacions')
    print(f'Modificar làrea del lavabo i imprimir la nova list area')
    print(f'Afegir làrea de pati interior i 2.78 a les últimes posicions. Imprimir la nova list area.')
    print(f'Imprimir el total de làrea del pis.')
    
#ejercicio14()

#Ejercicio 15: 
def ejercicio15():
    print('Vas a ir introduciendo nombres hasta que te canses!')
    dic_nomEdat = {}
    while True:
        nom = input('Introduce un nombre: \n')
        try:
            edad = int(input("Introduce una edad: "))
        except ValueError:
            print("La edad que has introducido no es un número entero.")
            continue
        dic_nomEdat.update({nom: edad})
        print(f'Diccionario de nombres hasta ahora: {dic_nomEdat}\n')
        cont = input('Quieres continuar? pulsa S para continuar.')
        if cont != 's':
            print(f'Fin del juego. \nNombres guardados en diccionario: {dic_nomEdat}')
            break

#ejercicio15()

#Ejercicio 16: 
def ejercicio16():
    while True:
        nums_frase =(input('Introduce 10 numeros separados por un espacio: \n'))
        try:
            nums = [int(num) for num in nums_frase.split()]
        except ValueError:
            print('Has introducido algun valor incorrecto, prueba de nuevo.')
            continue
        sumaTotal=0
        sumaTotal =sum(nums)
        mitjana = sumaTotal/len(nums)
        print(f'Numero introducidos por usuario: {nums}')
        print(f'Suma total de los numeros: {sumaTotal}')
        print(f'Mitjana total: {mitjana}')      
        break
    
#ejercicio16()


#Ejercicio 17:
def ejercicio17():
    nums_frase =(input('Introduce 10 numeros separados por un espacio: \n'))
    nums = [int(num) for num in nums_frase.split()]
    lista_aux = []
    max_num=float('-inf')
    aux_num=0
    for i in range(0, len(nums)-1):
        numA= nums[i]
        numB = nums[i + 1]
        lista_aux.append((numA, numB))  
        aux_num = sum(lista_aux[-1])  
        if aux_num > max_num:
                max_num = aux_num
    
    print(f'La mayor suma es: {max_num}')
    
ejercicio17()            


#Ejercicio 18:
from funciones import suma
#print(suma(1,2))

#Ejercicio 19:
from funciones import mostra_num
# mostra_num()

#Ejercicio 20:
from funciones import nom
# nom()

#Ejercicio 21: 
def ejercicio21(num_eur, iva_aplicat):
    try:
        iva_total = num_eur * (iva_aplicat / 100)
    except TypeError:
        print('Has introducido algun valor incorrecto, se te aplica el 21%')
        iva_total = num_eur * (21 / 100)
    
    print(f'Valor introducido: {num_eur}€') 
    print(f'IVA Introducido: {iva_total}%')
    print(f'Valor final: {num_eur - iva_total}')

#ejercicio21(100,'hola')

#Ejercicio 22: 
def ejercicio22():
    lista_nums=[0,1,2,3,4,5,6,7,8,9]
    new_list = []
    for i in range(0,10):
        square = pow(i,2)
        new_list.append(square)
    print(new_list)
    return new_list

#ejercicio22()

#Ejercicio23:
def ejercicio23():
    dict= {100: 10, 250: 5, 1500: 30}
    new_values= []
    values_iva=[]
    try:
        valor_iva= int(input('Introduce un valor de Iva:'))
    except ValueError:
        print('Has introducido algun valor incorrecto, se te aplica el 21%')
        valor_iva = 21
    
    for precio, descuento in dict.items():
        precio_con_descuento = precio - (precio * (descuento / 100))
        new_values.append(precio_con_descuento)
    
    for i in new_values:
        values_iva.append(i + (i * (valor_iva/100)))
    for n in range(len(dict)):
        print(f'El valor {n}: Precion con descuento: {new_values[n]}, precio con Iva: {values_iva[n]}')
        
#ejercicio23()

#Ejercicio24:
def ejercicio24():
    frase = input('Introduce una frase: ')
    new_list = frase.split()
    diccionario = {palabra: len(palabra) for palabra in new_list}
    print(diccionario)

#ejercicio24()

#Ejerciocio 25: 
import xml.etree.ElementTree as et
def ejercicio25():
    nombres = ['Ana', 'Luis', 'María', 'Javier', 'Elena']
    apellidos = ['González', 'Martínez', 'Fernández', 'López', 'Rodríguez']
    emails = ['ana@gmail.com', 'luis@hotmail.com', 'maria@yahoo.com', 'javier@example.com', 'elena@domain.com']
    dnis= ['12345678A', '98765432B', '56789012C', '34567890D', '21098765E']

    root= et.Element('students')
    
    for i in range(0,5):
        student = et.SubElement(root, 'student')
        name= et.SubElement(student, 'name')
        name.text= (f'{nombres[i]}')

        surname = et.SubElement(student, 'surname')
        surname.text = (f'{apellidos[i]}')

        email = et.SubElement(student, 'email')
        email.text = (f'{emails[i]}')

        dni = et.SubElement(student, 'Dni')
        dni.text=(f'{dnis[i]}')

    tree= et.ElementTree(root)
    tree.write('student.xml')
    
    with open ('student.xml', 'r') as file:
        xml_content = file.read()
        print(xml_content)
        
#ejercicio25()



    
    