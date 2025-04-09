'''
Autor: Andrea Johanna Duarte Guerrero.
Versión: 1.
Fecha de realización: 9/4/2025.
'''

import funciones as f
import clases as clas

lista_estudiantes = []

while True:
    opcion = f.mostrar_menu()

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = f.validar_edad(input("Edad: "))
        carrera = input("Carrera: ")
        estudiante = clas.Estudiante(nombre, edad, carrera)
        lista_estudiantes.append(estudiante)
        print("Estudiante registrado con éxito.")

    elif opcion == "2":
        nombre = input("Nombre del estudiante: ")
        estudiante = f.buscar_estudiante(lista_estudiantes, nombre)
        if estudiante:
            try:
                nota = float(input("Ingrese la nota: "))
                estudiante.agregar_calificacion(nota)
            except ValueError:
                print("La nota debe ser un número.")
        else:
            print("Estudiante no encontrado.")

    elif opcion == "3":
        nombre = input("Nombre del estudiante: ")
        estudiante = f.buscar_estudiante(lista_estudiantes, nombre)
        if estudiante:
            estudiante.mostrar_info()
        else:
            print("Estudiante no encontrado.")

    elif opcion == "4":
        if lista_estudiantes:
            for est in lista_estudiantes:
                est.mostrar_info()
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
