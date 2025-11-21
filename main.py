from cuadrado import Cuadrado
from rectangulo import Rectangulo

def sumar_areas(figuras):
    total_area = 0
    for figura in figuras:
        total_area += figura.area()
    return total_area

def sumar_perimetros(figuras):
    total_perimetro = 0
    for figura in figuras:
        total_perimetro += figura.perimetro()
    return total_perimetro

if __name__ == "__main__":
    print("--- INICIO DEL TALLER ---")
    
    # 1. Crear figuras
    c1 = Cuadrado(4)
    c2 = Cuadrado(10)
    r1 = Rectangulo(5, 8)
    r2 = Rectangulo(2, 6)
    
    lista = [c1, c2, r1, r2]

    # 2. Mostrar datos
    print("\n--- DETALLES ---")
    for fig in lista:
        print(f"{fig} | Área: {fig.area()} | Perímetro: {fig.perimetro()}")

    # 3. Pruebas de error (Validaciones)
    print("\n--- PRUEBA DE ERRORES ---")
    try:
        error = Cuadrado(-5)
    except ValueError as e:
        print(f"Error detectado: {e}")

    # 4. Resultados Totales
    print("\n--- TOTALES ---")
    print(f"Suma Áreas: {sumar_areas(lista)}")
    print(f"Suma Perímetros: {sumar_perimetros(lista)}")
