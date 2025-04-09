class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre  
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        if 0 <= nota <= 100:  
            self.calificaciones.append(nota)  #se utiliza la funcion append para agregar la calificacion a la lista 
        else:
            print("La nota debe estar entre 0 y 100.")

    def promedio(self):  
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0.0

    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}")  #formato para imprimir dos decimales
