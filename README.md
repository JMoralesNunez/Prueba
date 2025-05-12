# Instrucciones del programa.

Al comenzar el programa te encontrarás con un menú, y la pregunta de la opción que deseas, se espera que el usuario ingrese un número correspondiente a cada opción del menú.

### Ejemplo: 
- Sistema: Selecciona una opción: 1/2/3/4/5/6/7 
- Respuesta esperada del Usuario: 1

## Cada opción corresponde a un proceso diferente, después de terminar un proceso, se volverá al menú principal:

## Opción 1, añadir un producto:

### Pregunta1: Ingresa el nombre del producto.
- Respuesta esperada: Cualquier combinación de letras. Si se ingresa un número o un producto que ya esté dentro del inventario el sistema no dejará añadirlo.

### Pregunta2: Ingresa el precio del producto.
- Respuesta esperada: Se espera un número positivo, se aceptan números con decimales.

### Pregunta3: Ingresa la cantidad de producto.
- Respuesta esperada: Se espera un número positivo por encima de cero, no se aceptan decimales.

### Confirmación de producto añadido.

### Pregunta4: ¿Te gustaría añadir otro producto? 1.Si/2.No:
- Respuesta esperada: Se espera el número 1 ó 2. En caso de recibir el número 1, se repetirá el proceso anterior de añadir producto; en caso de recibir 2, volveremos al menú principal.

## Opción 2, Ver todos los productos:

- Al seleccionar esta opción, se mostrarán todos los productos que haya actualmente en el inventario. En caso de no haber productos, se informará de ello.

## Opción 3, Buscar un producto:

### Pregunta1: Ingresa el nombre del producto.
- Respuesta esperada: El nombre del producto a buscar, se espera una combinación de letras. En caso de recibir un número, éste no será válido y se pedirá el nombre del producto nuevamente; en caso de recibir el nombre de un producto que no exista en el inventario, se infomará de ello y devolverá al usuario al menú principal.

### El sistema mostrará el nombre, precio y cantidad del producto buscado.

## Opción 4, Actualizar precios:

### Pregunta1: Ingresa el nombre del producto.
- Respuesta esperada: El nombre del producto a cambiar su precio, se espera una combinación de letras. En caso de recibir un número o el nombre de un producto que no exista en el inventario, éste no será válido y se pedirá el nombre del producto nuevamente.

### El sistema mostrará el precio actual del producto.

### Pregunta 2: Ingresa el nuevo precio del producto.
- Respuesta esperada: Se espera un número positivo, se aceptan números con decimales.

### El sistema actualizará el precio del producto y mostrará un mensaje de confirmación.

## Opción 5, Borrar productos:

### Pregunta: ¿Deseas borrar un sólo producto o todo el inventario?
- Respuesta esperada: Se espera el número 1 ó 2.

### Respuesta 1:
#### Pregunta1: Ingresa el nombre del producto a eliminar.
- Respuesta esperada: El nombre del producto a eliminar, se espera una combinación de letras. En caso de recibir un número o el nombre de un producto que no exista en el inventario, éste no será válido y se pedirá el nombre del producto nuevamente.

#### El sistema borrará el producto y todos sus datos, y mostrará la confirmación de esto.

### Respuesta 2:
#### El sistema borrará todos los productos del inventario y mostrará confirmación de esto

## Opción 6, Calcular valor total del inventario:

### El sistema mostrará el valor total de cada producto, y el valor total del inventario.

## Opción 7, Salir:

### Mensaje de despedida del sistema, y finalización del programa.




