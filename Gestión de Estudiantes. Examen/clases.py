class Estudiante: 
    def __init__(self, nombre, edad, carrera, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = calificaciones
    
    def agregar_calificacion (self):
        while {self.nota} < 0 or {self.nota}>100: 
            if({self.nota}>0 or {self.nota}<100):
                self.nota = input("Ingrese la nota: ")
                break
            else:
                print("Nota inválida. ")


    def promedio():
        