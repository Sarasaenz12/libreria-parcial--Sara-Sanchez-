Respuesta SM-1:

La respuesta correcta seria la C el enfoque descrito es desarrollo tradicional con pruebas al final, El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas.

Porque en este enfoque las pruebas se realizan al final del desarrollo, lo que provoca que los errores se detecten tarde y corregirlos sea mucho más costoso.

Respuesta SM-2:

La respuesta correcta seria la B La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera.

Porque en TDD primero se debe escribir un test que falle antes de crear el código de producción, y en este caso el desarrollador implementó la función completa antes de escribir cualquier prueba.

PREGUNTAS ABIERTAS:

PA-1:

En TDD el paso GREEN lo que busca es que el test pase la prueba con la minima implementacion para poder validar que el test pase, lo ideal en TDD es que en el GREEN no se ponga la logica mas extensa o compleja por eso aunque este codigo de GREEN  sea feo es aceptable mientras el test pase la prueba, despues de este el paso a seguir seria el REFACTOR ya que este si mejora la calidad del codigo que se hizo en el GREEN y con esto se mejora la calidad sin romper la prueba, si el desarrollador escribe codigo limpio rompe lo que es el TDD ya que esto lo que hace es agregar funcionales que no son necesarias y puede generar mas errores

PA-2:

La diferencia entre TDD u BDD es que en el TDD esta pensado mas para desarrolladores ya que ayuda a construir el codigo pasp a paso y saber que funcion debe de hacer mientras codifica y que esta haga lo que debe de hacer; mientras en el BDD se enfoca mas en el compartamiento del sistema desde la vista del usuario o del negocio asi cualquier perosna como el QA o losclientes entienden lo que se espera del sistema aqui en BDD suele describir esenarios en situaciones reales.

PA-3:

Tener una cobertura alta solo significa que muchas líneas de código fueron ejecutadas durante las pruebas pero no garantiza que las pruebas estén verificando correctamente el comportamiento del sistema, un programa puede tener 95% de cobertura y aun así contener errores importantes. 
Imagina una función que valida la contraseña de un usuario, Las pruebas ejecutan la función con varias entradas y verifican únicamente que el sistema no se bloquee ni arroje errores, sin embargo nunca comprueban si realmente está aceptando la contraseña correcta y rechazando la incorrecta.

PA-4:

Esa lógica es incorrecta porque probar un solo valor no garantiza que el sistema funcione correctamente en todos los casos especialmente en los límites donde suelen aparecer más errores; que el 20% funcione solo demuestra que ese caso específico pasa correctamente. Lo que realmente haria yo es probaría valores como 0% y 40% porque son los límites válidos definidos por la regla y es importante confirmar que el sistema los acepte ademas deberia de probar valores inválidos como -1% y 41% para verificar que el sistema los rechace correctamente, asi estaria desarrollando las pruebas y haria serian esas e esta manera se cubren tanto casos válidos como inválidos y se reducen las posibilidades de que existan errores ocultos en los extremos.

PA-5:

Las pruebas ágiles, TDD y BDD son importantes para que CI/CD funcione correctamente, porque todas buscan que el software pueda verificarse de manera automática y continua hacinedo el sistema con TDD y BDD el equipo crea pruebas desde el inicio del desarrollo, lo que permite detectar errores rápidamente cada vez que alguien hace cambios en el código, en un pipeline de CI/CD, esas pruebas se ejecutan automáticamente antes de integrar o desplegar una nueva versión. Si el equipo no tiene una suite de pruebas automatizadas sólida, el pipeline pierde confiabilidad porque podrían llegar errores a producción sin ser detectados, tambien hay que considerar que cada cambio tendría que revisarse manualmente, haciendo el proceso más lento, tedioso e inseguro y propenso a fallos.
