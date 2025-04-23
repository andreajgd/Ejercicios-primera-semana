import os
# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar al inicio
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Método que cuenta los nodos
    def longitudLista(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        print(f"Cantidad de nodos en la lista: {contador}")

    # Verificar si la lista está vacía
    def esta_vacia(self):
        if not self.cabeza:
            print("La lista está vacía")
        else:
            print("La lista NO está vacía")

    # Imprimir el último valor de la lista
    def imprimir_ultimo(self):
        if not self.cabeza:
            print("La lista está vacía")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        print(f"Último valor de la lista: {actual.valor}")

def menu():
    
    lista = ListaEnlazada()
    print("Ingresa los elementos iniciales para la lista (separados por espacio):")
    elementos = input().split()
    for e in elementos:
        lista.insertar(e)

    while True:
        print("\n", "-"*10, "MENÚ", "-"*10)
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Eliminar un valor")
        print("4. Buscar un valor")
        print("5. Contar nodos")
        print("6. Verificar si la lista está vacía")
        print("7. Imprimir el último valor")
        print("8. Imprimir la lista")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            val = input("Valor a insertar al inicio: ")
            lista.insertar_inicio(val)
        elif opcion == "2":
            val = input("Valor a insertar al final: ")
            lista.insertar(val)
        elif opcion == "3":
            val = input("Valor a eliminar: ")
            if lista.eliminar(val):
                print("Valor eliminado.")
            else:
                print("Valor no encontrado.")
        elif opcion == "4":
            val = input("Valor a buscar: ")
            if lista.buscar(val):
                print("Valor encontrado.")
            else:
                print("Valor no encontrado.")
        elif opcion == "5":
            lista.longitudLista()
        elif opcion == "6":
            lista.esta_vacia()
        elif opcion == "7":
            lista.imprimir_ultimo()
        elif opcion == "8":
            lista.imprimir()
        elif opcion == "9":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

"""Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente, y no cuando es importado como módulo en otro archivo"""
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()