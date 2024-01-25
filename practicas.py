import random

#Ejercicio 1: 
print('Hello World')

#Ejercicio 2: 
# num1 = int(input('Introduce el primer numero: \n' ))
# num2 = int(input('Introduce el segundo numero: \n' ))
# print(f'La suma de los numeros es: {num1+num2}')

#Ejercicio 3: 
# frase = input('Introduce una frase: \n')
# frase_2 = frase.replace(' ', '')
# print(f'Frase sin espacio: {frase_2}')

#Ejercicio 4: 
# for i in range(0,501):
#     if i%2 != 0: 
#         print(i)


#Ejercicio 5:
# num_eur = float(input('Introduce un numearo en €: '))
# iva_aplicat = int(input('Introduce el IVA a aplicar: '))
# iva_total = num_eur * (iva_aplicat / 100)
# print(f'Valor introducido: {num_eur}€') 
# print(f'IVA Introducido: {iva_total}%')
# print(f'Valor final: {num_eur - iva_total}')


#Ejercicio 6:
# palabra_1 = input('Introduce una palabra: \n')
# palabra_2 = input('Introduce una palabra: \n')
# print(f'Palabra 1 tiene: {len(palabra_1)} letras.')
# print(f'Palabra 2 tiene: {len(palabra_2)} letras.')
# print(f'La primera letra de {palabra_1} es : {palabra_1[0]}')
# print(f'La primera letra de {palabra_2} es : {palabra_1[0]}')

#Ejercicio 7: 
# palabra = input('Introduce una palabra o frase: \n')
# palabra_inver = palabra[::-1]
# if palabra == palabra_inver:
#     print(f'La palabra/frase que has introducido es un palindromo!')
#     print(palabra_inver)
# else:
#     print(f'{palabra}: palabra que has introducido, no es un palindromo: {palabra_inver}')    


#Ejercicio 8:
def adivina_numero():
    numero_aleatorio = random.randint(1, 100) 
    while True:
        user_num = input('Introduce un numero para adivinar mi numero secreto!\n')
        if user_num.isdigit():
            user_num = int(user_num)
        else:
            print("Por favor, introduce un número entero válido.")
        
        if numero_aleatorio == user_num:
            print(f'Enhorabuena has adivinado el numero! Era el {numero_aleatorio}')
            break
        elif user_num > numero_aleatorio:    
            print("El numero que has introducido es MAYOR al mio")
        else:
            print('El numero introducido es MENOr al mio')

            
        print('*'*100)
        
adivina_numero()