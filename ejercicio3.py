#. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por la compra de más de 3 
# docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso 
# sobre 3. Diseñe un programa que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio 
# por la compra de cierta cantidad de docenas del producto.


op =0
while op == 1:
    print("Venta al por mayor. ")
    
    cantidad= int(input("Escribe la cantidad de docenas a adquirir: "))
    if(cantidad < 1):
        print("Por favor ingresa una cantidad valida.")
    # if(cantidad <3):
    #     desc = 
 