Feature: Cálculo de precio final en la Librería del Centro
  Como administrador de la Librería del Centro
  Quiero aplicar descuentos e IVA a mis productos
  Para que el precio final que ve el cliente sea siempre correcto

  Background:
    Given un producto llamado "Libro Python" con precio base de 100.0

  @critical
  Scenario: Descuento del 0% es válido y no modifica el precio
    When se aplica un descuento del 0%
    Then el precio con descuento es 100.0

  @critical
  Scenario: Descuento del 40% es válido y se aplica correctamente
    When se aplica un descuento del 40%
    Then el precio con descuento es 60.0

  @critical
  Scenario: Descuento mayor al 40% es rechazado por el sistema
    When se intenta aplicar un descuento del 41%
    Then el sistema rechaza el descuento con un error

  @smoke
  Scenario: Precio final aplica descuento e IVA en el orden correcto
    When se aplica un descuento del 20%
    Then el precio final es 95.2

  @smoke
  Scenario Outline: Verificacion del precio final con distintos descuentos
    When se aplica un descuento del <descuento>%
    Then el precio final es <precio_final>

    Examples:
      | descuento | precio_final |
      | 0         | 119.0        |
      | 10        | 107.1        |
      | 40        | 71.4         |