#. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 
# docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso 
# sobre 3. Diseñe un programa que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio 
# por la compra de cierta cantidad de docenas del producto.

import os 
os.system('cls' if os.name == 'nt' else 'clear')

op =1
docena = 1500

while op == 1:
    print("Venta al por mayor. ")
    
    cant= int(input("Escribe la cantidad de docenas a adquirir: "))
    if(cant < 1):
        print("Por favor ingresa una cantidad valida.")
        continue
    elif(cant <3):
        cantidad = cant * docena
        desc = cantidad -  (0.1* cantidad)
        print(f"El precio de las {cant} docenas es: {desc}")
    elif (cant == 3):
        cantidad = cant * docena
        desc = cantidad - (0.15* cantidad)
        print(f"El precio de las {cant} docenas es: {desc}")
    elif (cant > 3):
        cantidad = cant * docena
        desc = cantidad - (0.15* cantidad)
        obsequio = (cant-3)/3 
        print(f"El precio de las {cant} docenas es: {desc}, y {obsequio} unidades de obsequio!")
    
    op = int(input("Desea comprar de nuevo? 1: sí, 2: salir: "))

print("Saliste del programa. ")

 