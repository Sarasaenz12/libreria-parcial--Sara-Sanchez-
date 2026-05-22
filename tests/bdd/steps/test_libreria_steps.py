import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../'))

import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from src.producto import Producto, DescuentoInvalidoError

scenarios('../features/libreria.feature')


@pytest.fixture
def ctx():
    return {"producto": None, "error": None}


@given(parsers.parse('un producto llamado "{nombre}" con precio base de {precio:g}'))
def crear_producto(ctx, nombre, precio):
    ctx["producto"] = Producto(nombre, precio)


@when(parsers.parse('se aplica un descuento del {descuento:g}%'))
def aplicar_descuento(ctx, descuento):
    ctx["producto"].aplicar_descuento(descuento)


@when(parsers.parse('se intenta aplicar un descuento del {descuento:g}%'))
def intentar_descuento(ctx, descuento):
    try:
        ctx["producto"].aplicar_descuento(descuento)
        ctx["error"] = None
    except DescuentoInvalidoError as e:
        ctx["error"] = e


@then(parsers.parse('el precio con descuento es {valor:g}'))
def verificar_precio_con_descuento(ctx, valor):
    assert ctx["producto"]._precio_con_descuento() == pytest.approx(valor)


@then(parsers.parse('el precio final es {valor:g}'))
def verificar_precio_final(ctx, valor):
    assert ctx["producto"].calcular_precio_final() == pytest.approx(valor)


@then("el sistema rechaza el descuento con un error")
def verificar_error_descuento(ctx):
    assert isinstance(ctx["error"], DescuentoInvalidoError)