#Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número.


import os 
os.system('cls' if os.name == 'nt' else 'clear')
op = 1

while op == 1:
    print("+-"*50)
    print("Este programa determina si el número es igual al revés.")
    print("Escribe un número de 3 cifras. ")
    print("+-"*50)
    num = int(input("Escribe un número: "))

    if 100 <= num <= 999:
        unidad = num % 10         
        decena = (num // 10) % 10  
        centena = num // 100        
        
        num_invertido = (unidad * 100) + (decena * 10) + centena

        if num == num_invertido:
            print(f"{num} es igual al revés. \n{num} = {num_invertido}.")
        else:
            print(f"{num} no es igual al revés.\n{num} != {num_invertido}.")

    else:
        print("Debes ingresar un número de 3 cifras.")
    

    op = int(input("1= Ingresar otro número, 2= Salir."))

print("Saliste del programa.")