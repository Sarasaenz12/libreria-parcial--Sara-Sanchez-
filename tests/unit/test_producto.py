import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.producto import Producto, PrecioInvalidoError, DescuentoInvalidoError


@pytest.fixture
def producto():
    return Producto("Libro Python", 100.0)


class TestPrecioBase:

    def test_CP01_precio_valido_crea_producto(self):
        p = Producto("Libro", 50.0)
        assert p.precio_base == 50.0

    def test_CP02_precio_cero_lanza_error(self):
        with pytest.raises(PrecioInvalidoError):
            Producto("Libro", 0.0)

    def test_CP03_precio_negativo_lanza_error(self):
        with pytest.raises(PrecioInvalidoError):
            Producto("Libro", -10.0)

class TestDescuento:

    def test_CP04_descuento_cero_es_valido(self, producto):
        producto.aplicar_descuento(0)
        assert producto._descuento == 0

    def test_CP05_descuento_40_es_valido(self, producto):
        producto.aplicar_descuento(40)
        assert producto._descuento == 40

    def test_CP06_descuento_41_lanza_error(self, producto):
        with pytest.raises(DescuentoInvalidoError):
            producto.aplicar_descuento(41)

    def test_descuento_negativo_lanza_error(self, producto):
        with pytest.raises(DescuentoInvalidoError):
            producto.aplicar_descuento(-1)