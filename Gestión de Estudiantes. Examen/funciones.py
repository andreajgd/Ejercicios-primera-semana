def mostrar_menu():
    print("\n" + "-" * 20 + " MENÚ " + "-" * 20)
    print("1. Registrar nuevo estudiante.")
    print("2. Agregar calificación a un estudiante.")
    print("3. Mostrar información de un estudiante.")
    print("4. Mostrar todos los estudiantes.")
    print("5. Salir del programa.")
    print("-"*20, "-"*20)
    opcion = input("Opción: ")
    return opcion


def validar_edad(entrada):
    while True:
        try:
            edad = int(entrada)  #verifica que la conversion a entero se pueda
            if edad > 0: #verifica que sea mayor que 0 
                return edad
            else:
                print("La edad debe ser un número positivo.")
        except ValueError:  #en caso que no se pueda convertir a entero, se vuelve a pedir el valor
            print("Ingrese un número válido.")
        entrada = input("Edad: ")


def buscar_estudiante(lista, nombre):
    for est in lista:
        if est.nombre.lower() == nombre.lower():  #se utiliza la funcion . lower para encontrar el nombre, independientemente qu esea en inuscula o mayuscula
            return est
    return None
