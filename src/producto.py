class PrecioInvalidoError(ValueError):
    pass

class DescuentoInvalidoError(ValueError):
    pass

class Producto:

    PRECIO_MINIMO = 0
    DESCUENTO_MINIMO = 0
    DESCUENTO_MAXIMO = 40

    def __init__(self, nombre: str, precio_base: float):
        self._validar_precio(precio_base)
        self.nombre = nombre
        self.precio_base = precio_base
        self._descuento = 0

    def _validar_precio(self, precio: float) -> None:
        """Lanza PrecioInvalidoError si el precio no es mayor que cero."""
        if precio <= self.PRECIO_MINIMO:
            raise PrecioInvalidoError(
                f"El precio base debe ser mayor que cero. Se recibió: {precio}"
            )

    def _validar_descuento(self, descuento: float) -> None:
        """Lanza DescuentoInvalidoError si el descuento esta fuera del rango permitido."""
        if descuento < self.DESCUENTO_MINIMO or descuento > self.DESCUENTO_MAXIMO:
            raise DescuentoInvalidoError(
                f"El descuento debe estar entre {self.DESCUENTO_MINIMO}% "
                f"y {self.DESCUENTO_MAXIMO}%. Se recibió: {descuento}%"
            )

    def aplicar_descuento(self, descuento: float) -> None:
        """Aplica un descuento porcentual al producto."""
        self._validar_descuento(descuento)
        self._descuento = descuento

    def calcular_precio_final(self) -> float:      # ← único método nuevo
        precio_con_descuento = self.precio_base * (1 - self._descuento / 100)
        return precio_con_descuento * 1.19