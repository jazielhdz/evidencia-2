import re

class Vehiculo:
    def __init__(self, unidad, marca, modelo, km):
        self.unidad = unidad
        self.marca = marca
        self.modelo = modelo
        self.km = km

    def recorrido(self, n):
        if n > 0:
            self.km += n
        else:
            print("el número de kilómetros debe ser positivo")

def validar_unidad():
    while True:
        unidad = input("ingrese el codigo de identificacion de la unidad (XX-123): ")
        if re.match(r"^[A-Za-z0-9]{2}-[A-Za-z0-9]{3}$", unidad):
            return unidad
        else:
            print("codigo de unidad inválido, debe tener el formato XX-123 con letras o números.")

def validar_marca():
    marca = input("ingrese la marca de la unidad: ")
    return marca

def validar_modelo():
    while True:
        try:
            modelo = int(input("ingrese el año de fabricación (2020-2024): "))
            if 2020 <= modelo <= 2024:
                return modelo
            else:
                print("año de fabricacion invalido, debe estar entre 2020 y 2024.")
        except ValueError:
            print("entrada invalida, por favor, ingrese un año como un número entero.")

def validar_km():
    while True:
        try:
            km = int(input("ingrese los kilometros recorridos: "))
            if km >= 0:
                return km
            else:
                print("los kilometros deben ser un numero entero positivo.")
        except ValueError:
            print("entrada invalida, por favor, ingrese un número entero.")


def main():
    unidades = []
    try:
        cantidad = int(input("ingrese la cantidad de unidades de transporte a dar de alta: "))
        for _ in range(cantidad):
            print("\ningrese los datos de la unidad:")
            unidad = validar_unidad()
            marca = validar_marca()
            modelo = validar_modelo()
            km = validar_km()
            unidades.append(Vehiculo(unidad, marca, modelo, km))

        print("\nUnidades registradas:")
        for i, unidad in enumerate(unidades, start=1):
            print(f"Unidad {i}: {unidad.unidad}, Marca: {unidad.marca}, Modelo: {unidad.modelo}, Km: {unidad.km}")

    except ValueError:
        print("entrada invalida, ingrese un número entero para la cantidad de unidades.")

if __name__ == "__main__":
    main()
