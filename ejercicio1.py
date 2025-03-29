'''
1. Desarrolla un programa que calcule el importe a pagar por un vehículo al circular por una autopista. 
El vehículo puede ser una bicicleta, una moto, un carro o un camión. Para definir el conjunto de vehículos
 deben utilizar una estructura adecuada. El importe se calculará según los siguientes datos:

a) Un importe fijo de 100 córdobas para la bicicleta.
b) Las motos y los carros pagarán 30 córdobas por Km.
c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas.

'''
import os 
os.system('cls' if os.name == 'nt' else 'clear')


op = 1
while op == 1:
    print("1. Bicicleta. ")
    print("2. Moto. ")
    print("3. Carro. ")
    print("4. Camiones. ")
    tipo = int(input("Opción: "))
    if(tipo == 1):
        print("Debes pagar C$100.")
    if ( tipo == 2 or tipo == 3):
        km = float(input("Cuantos kilometros recorriste? "))
        total = km *30
        print(f"Debes pagar C${total}.")
    if (tipo == 4):
        km = float(input("Cuantos kilometros recorriste? "))
        ton = float(input("Cuantas toneladas tienes? "))
        total = (km *30) + ( ton *25)
        print(f"Debes pagar C${total}.")
    
    op = int(input ("Salir del programa (0), Continuar (1): "))

print("Saliste del programa.")
