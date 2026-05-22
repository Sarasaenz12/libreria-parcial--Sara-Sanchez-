class PrecioInvalidoError(ValueError):
    pass

class Producto:

    PRECIO_MINIMO = 0

    def __init__(self, nombre: str, precio_base: float):
        self._validar_precio(precio_base)
        self.nombre = nombre
        self.precio_base = precio_base

    def _validar_precio(self, precio: float) -> None:
        """Lanza PrecioInvalidoError si el precio no es mayor que cero."""
        if precio <= self.PRECIO_MINIMO:
            raise PrecioInvalidoError(
                f"El precio base debe ser mayor que cero. Se recibió: {precio}"
            )