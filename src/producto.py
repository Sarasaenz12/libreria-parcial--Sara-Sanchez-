class PrecioInvalidoError(ValueError):
    pass

class Producto:

    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise PrecioInvalidoError(
                f"El precio base debe ser mayor que cero. Se recibió: {precio_base}"
            )
        self.nombre = nombre
        self.precio_base = precio_base