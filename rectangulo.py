from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def __str__(self):
        return f"Rectangulo [Ancho: {self.ancho}, Alto: {self.alto}]"
