'''
2. Escribir un programa que permita emitir la FACTURA correspondiente,
 a una compra de un artículo determinado, del que se adquieren una o varias unidades.
  El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad), es mayor de 1000,
  se aplicará un descuento del 12%.
'''

import os 
os.system('cls' if os.name == 'nt' else 'clear')

total =0
stotal =0
op =1 

def precio(total):
    porcentaje = stotal*1.15

    if(stotal > 1000):
        porcentaje = total*0.15
        total -= porcentaje

    return total 

while op ==1: 
 
    print("1. Camiseta. ----- C$100")
    print("2. Zapatos. ------C$500 ")
    print("3. Pantalon.-----C$300 ")
    print("4. Reloj. ------C$600")
    opc = int(input("Opción: "))
    if(opc == 1):
        stotal += 100
    elif(opc == 2):
        stotal += 500
    elif (opc== 3):
        stotal += 300
    elif (opc== 4):
        stotal += 600
    else:
        print("Opción no válida. Intenta de nuevo.")
        continue 
    
    total = precio(stotal) 
    
    op = int(input(f"Tu total es de: {total} + IVA \n Deseas agregar algo más al carrito (1= si, 0=no)"))
