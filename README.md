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