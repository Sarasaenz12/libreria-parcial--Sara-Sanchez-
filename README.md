## Analisis y respuesta a preguntas

### Tabla de participaciones (Regla 1 y Regla 2):

| Partición | Rango | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida — precio normal | (0, +∞) | 50.0 | Producto creado sin error |
| Inválida — precio cero | 0 | 0.0 | `PrecioInvalidoError` |
| Inválida — precio negativo | (−∞, 0) | −10.0 | `PrecioInvalidoError` |

---

### Participaciones de equivalencia (Regla 2):

| Partición | Rango | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida — descuento normal | (0, 40) | 20 | Descuento aplicado correctamente |
| Válida — descuento mínimo exacto | 0 | 0 | Precio base sin cambio |
| Válida — descuento máximo exacto | 40 | 40 | Descuento máximo aplicado |
| Inválida — supera el máximo | (40, +∞) | 50 | `DescuentoInvalidoError` |
| Inválida — descuento negativo | (−∞, 0) | −5 | `DescuentoInvalidoError` |

---

### Valores limite

| Valor | Posición | Resultado esperado |
|---|---|---|
| -1% | Justo antes del límite inferior | `DescuentoInvalidoError` |
| 0% | Límite inferior exacto | Descuento aplicado correctamente |
| 1% | Justo después del límite inferior | Descuento aplicado correctamente |
| 39% | Justo antes del límite superior | Descuento aplicado correctamente |
| 40% | Límite superior exacto | Descuento aplicado correctamente |
| 41% | Justo después del límite superior | `DescuentoInvalidoError` |

---

## Respuesta a la pregunta 

¿El IVA del 19% se aplica a todos los productos sin excepción, o hay categorías exentas como libros o medicamentos?

Justificacion: Si existen productos exentos de IVA, la lógica de `calcular_precio_final()` cambia y necesito casos de prueba para ambos caminos

---

## Casos de prueba

---

## PARTE 2 — Tabla de casos de prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP-01 | R1 | Precio válido crea el producto correctamente | Ninguna | nombre="Libro", precio=50.0 | Crear `Producto("Libro", 50.0)` | Producto creado, precio_base=50.0 | Positivo |
| CP-02 | R1 | Precio cero es rechazado | Ninguna | nombre="Libro", precio=0.0 | Crear `Producto("Libro", 0.0)` | Se lanza `PrecioInvalidoError` | Negativo |
| CP-03 | R1 | Precio negativo es rechazado | Ninguna | nombre="Libro", precio=-10.0 | Crear `Producto("Libro", -10.0)` | Se lanza `PrecioInvalidoError` | Negativo |
| CP-04 | R2 | Descuento del 0% es válido y no cambia el precio | Producto con precio=100.0 | descuento=0 | `aplicar_descuento(0)` | Descuento aplicado, precio sin cambio | Borde |
| CP-05 | R2 | Descuento del 40% es válido | Producto con precio=100.0 | descuento=40 | `aplicar_descuento(40)` | Descuento aplicado correctamente | Borde |
| CP-06 | R2 | Descuento del 41% es rechazado | Producto con precio=100.0 | descuento=41 | `aplicar_descuento(41)` | Se lanza `DescuentoInvalidoError` | Negativo |
| CP-07 | R3 | Precio final aplica descuento 20% e IVA 19% | Producto precio=100.0, descuento=20% | ninguno | `calcular_precio_final()` | (100 × 0.80) × 1.19 = 95.2 | Positivo |
| CP-08 | R3 | Precio final sin descuento solo aplica IVA | Producto precio=100.0, descuento=0% | ninguno | `calcular_precio_final()` | 100 × 1.19 = 119.0 | Borde |

