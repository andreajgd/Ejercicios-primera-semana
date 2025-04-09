lista_estudiante = []
calificaciones = []


def mostrar_menu():
    print("*-"*40, "MENÚ", "*-"*40)
    print("1. Registrar nuevo estudiante. ")
    print("2. Agregar calificación a un estudiante.")
    print("3. Mostrar información de un estudiante. ")
    print("4. Mostrar todos lo estudiantes. ")
    print("5. Salir del programa. ")
    op = int(input("Opción: "))
    
    match op:
        case 1:
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            carrera = input("Carrera: ")

        case 2: 
            nombre = input("Nombre: ")
            for c in calificaciones: 
                c = int(input(f"Nota{c+1}: "))
                calificaciones.append(c)

            

def validar_datos(edad):
     while edad < 0: 
            if(edad>0):
                edad = input("Ingrese la edad: ")
                break
            else:
                print("Edad inválida. ")

def buscar_estudiante(nombre):
    for i in lista_estudiante:
        if(i == nombre):
            print("Alumno encontrado.")
            
        else:
            print("No se encontró. ")