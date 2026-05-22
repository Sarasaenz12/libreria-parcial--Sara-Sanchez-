import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.producto import Producto, PrecioInvalidoError


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