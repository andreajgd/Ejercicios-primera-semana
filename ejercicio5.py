'''
Se desea escribir un programa para el cálculo del área de diversas superficies: cuadrado, rectángulo, círculo, triángulo y trapecio. 
'''
import math
import os 
os.system('cls' if os.name == 'nt' else 'clear')

def cuadrado(x):
    area = x**2
    return area

def circulo (x):
   total =  math.pi* (x**2)
   return total 

def rectangulo (b,h):
    total = b*h 
    return total 

def trapecio (b1,b2,h):
    total= (b1+b2)*h/2
    return total

def triangulo(b,h):
    total = (b*h)/2
    return total

op = 1
while op == 1: 
    print("="*40)
    print("CÁLCULO DE SUPERFICIES (versión 1.0)")
    print("="*40)
    print("1. Cuadrado.")
    print("2. Círculo.")
    print("3. Rectángulo.")
    print("4. Trapecio.")
    print("5. Triángulo.")
    print("="*40)
    opcion = int(input("Opción: "))
    
    if (opcion == 1):
        lado = int(input("Medida del lado: "))
        total = cuadrado(lado)
        print(f"El área del cuadrado es: {total}")

    elif (opcion == 2):
        radio = int(input("Medida del radio: "))
        total = circulo (radio)
        print(f"El área del círculo es: {total:.2f}")

    elif (opcion == 3):
        base = int(input("Base: "))
        h = int(input("Altura: "))
        total = rectangulo(base, h)
        print(f"El área del rectángulo es: {total}")

    elif( opcion == 4):
        b1 = int(input("Base 1: "))
        b2 = int(input("Base 2: "))
        h = int(input("Altura: "))
        total = trapecio(b1,b2,h)
        print(f"El área del trapecio es: {total}")
    
    elif( opcion == 5):
        b = int(input("Base: "))
        h = int(input("Altura: "))
        total = triangulo(b,h)
        print(f"El área del triángulo es: {total}")
    
    else:
        print("Opción no válida.")
        continue
    
    op = int(input ("Salir del programa (0), Continuar (1): "))

print("Saliste del programa.")