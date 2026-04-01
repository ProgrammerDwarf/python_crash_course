# Notas del capítulo 2: Variables y tipos de datos

En este capítulo se introducen los conceptos de variables y tipos de datos en Python. Se explica cómo crear variables para almacenar información y cómo asignar valores a estas variables. Además, se presentan los diferentes tipos de datos que existen en Python; empezando por las cadenas de caracteres (strings), números enteros (integers) y números de punto flotante (floats). 

Una parte que me pareció sumamente interesante fue la explicación sobre cómo ver a las variables, aquí el autor desmonta el ejemplo clásico de la caja con una etiqueta, y lo reemplaza por una metáfora más cercana a la realidad, que es la de un nombre que apunta a un valor en la memoria. Esto ayuda a entender mejor cómo funcionan las variables en Python y cómo se relacionan con los tipos de datos.

Resulta que cada vez que nombramos a una variable, lo que realmente estamos haciendo es crear una referencia a un valor en la memoria, y no una caja que contiene ese valor. Esto significa que si asignamos un nuevo valor a una variable que ya existía, por ejemplo: `nombre = "Reinid"` y luego `nombre = "Jenesis"`, lo que sucede es que la variable `nombre` ahora apunta a un nuevo valor en la memoria, y el valor anterior ("Reinid") queda sin referencia, lo que eventualmente puede ser limpiado por el recolector de basura de Python.

## Mejores prácticas para nombrar variables

Adicionalmente, se discuten las buenas prácticas para nombrar variables, como:
- Usar nombres descriptivos que indiquen el propósito de la variable. Ejemplo: `edad_usuario` en lugar de `e`.
- Evitar el uso de palabras reservadas del lenguaje. Ejemplo: `if`, `for`, `while`, etc.
- Utilizar el estilo de nomenclatura `snake_case` para mejorar la legibilidad. Ejemplo: `nombre_completo` en lugar de `nombreCompleto`.
- Mantener la consistencia en el estilo de nombres a lo largo del código. Ekjemplo: si se usa `snake_case` para una variable, no usar `camelCase` para otra.
- Evitar el uso excesivo de abreviaturas que puedan dificultar la comprensión del código. Ejemplo: `cantidad_productos` en lugar de `cant_prod`.
- No comenzar los nombres de las variables con números o caracteres especiales. Ejemplo: `1variable` no es válido, pero `variable1` sí lo es.
- Usar mayúsculas y minúsculas de manera consistente, ya que Python es sensible a ellas. Ejemplo: `Variable` y `variable` son dos variables diferentes.
- Evitar el uso de espacios en los nombres de las variables. Ejemplo: `nombre completo` no es válido, pero `nombre_completo` sí lo es.
- No usar guiones (`-`) en los nombres de las variables, ya que Python interpreta esto como una operación de resta. Ejemplo: `nombre-completo` no es válido, pero `nombre_completo` sí lo es.
- Utilizar prefijos o sufijos cuando sea necesario para indicar el tipo de dato o el propósito de la variable. Ejemplo: `is_active` para una variable booleana que indica si algo está activo.

En resumen, estA parte del capítulo proporciona una base sólida para entender cómo funcionan las variables y los tipos de datos en Python, así como las mejores prácticas para nombrar variables de manera efectiva y clara.

*Ejercicio propuesto:*
- 2.1 Crear una variable para almacenar tu nombre y otra para tu edad. Imprimir ambas variables en la consola.
- 2.2 Crear una variable para almacenar un texto y luego cambiar su valor. Imprimir el valor antes y después del cambio.

## Tipo de dato: Cadenas de caracteres (Strings)

Se da a entender que las cadenas de caracteres son secuencias de caracteres encerradas entre comillas simples (' ') o dobles (" "). Se pueden manipular utilizando diferentes métodos y funciones integradas en Python; es decir, todo en Python es tratado como un objeto por lo que tienen métodos asociados a ellos. Algunos ejemplos de metodos comunes para trabajar con cadenas de caracteres son:

- `len()`: Devuelve la longitud de la cadena. Ejemplo, `len("Hola")` devuelve `4`.
- `capitalize()`: Convierte el primer carácter de la cadena a mayúscula. Ejemplo, `"hola".capitalize()` devuelve `"Hola"`.
- `title()`: Convierte el primer carácter de cada palabra en mayúscula. Ejemplo, `"hola mundo".title()` devuelve `"Hola Mundo"`.
- `upper()`: Convierte todos los caracteres de la cadena a mayúsculas. Ejemplo, `"hola".upper()` devuelve `"HOLA"`.
- `lower()`: Convierte todos los caracteres de la cadena a minúsculas. Ejemplo, `"HOLA".lower()` devuelve `"hola"`.
- `strip()`: Elimina los espacios en blanco al inicio y al final de la cadena. Ejemplo, `"  hola  ".strip()` devuelve `"hola"`.
- `replace()`: Reemplaza una subcadena por otra dentro de la cadena. Ejemplo, `"hola mundo".replace("mundo", "Python")` devuelve `"hola Python"`.
- `split()`: Divide la cadena en una lista de subcadenas basándose en un separador. Ejemplo, `"hola mundo".split(" ")` devuelve `["hola", "mundo"]`.
- `join()`: Une una lista de cadenas en una sola cadena, utilizando un separador especificado.  Ejemplo, `", ".join(["hola", "mundo"])` devuelve `"hola, mundo"`.
- `find()`: Busca una subcadena dentro de la cadena y devuelve su posición. Ejemplo, `"hola mundo".find("mundo")` devuelve `5`.
- `format()`: Permite formatear cadenas de manera más legible y flexible. Ejemplo, `"Hola, {}. Tienes {} años.".format("Juan", 30)` devuelve `"Hola, Juan. Tienes 30 años."`.

### Formateo de cadenas: f-strings
Este último método ha venido siendo sustituido en gran medida por las f-strings, que son una forma más moderna y eficiente de formatear cadenas en Python. Las f-strings se introdujeron en Python 3.6 y permiten incrustar expresiones dentro de cadenas literales, utilizando la sintaxis `{}` precedida por una `f` antes de las comillas de apertura.

Un ejemplo de uso de f-strings sería:

```python
nombre = "Juan"
print(f"Hola, {nombre}!")
```         

Y si juntamos un ejemplo con algún otro método podríamos tener algo así:

```python
nombre = "juan"
print(f"Hola, {nombre.capitalize()}!")
```
Esto imprimiría: `Hola, Juan!`

En resumen, las cadenas de caracteres son un tipo de dato fundamental en Python y ofrecen una amplia variedad de métodos para manipular y trabajar con texto de manera eficiente.

*Ejercicio propuesto:*
- 2.3 Crea una frase e insertale un nombre de alguna persona a la quieras decir dicha frase.
- 2.4 Escoge el nombre de alguien que conozcas y modifica su nombre para que se vea en mayúsculas, minúsculas y con la primera letra en mayúscula.
- 2.5 Busca una cita famosa de alguien que admires e imprímela en la consola junto con el nombre del autor.
- 2.6 Repite el ejercicio 2.5, pero esta vez usa una variable para el nombre del autor y otra para el mensaje completo.
- 2.7 Crea una variable con el nombre de una persona que incluya espacios en blanco al inicio y al final. Imprime el nombre con los espacios y luego usa los métodos lstrip(), rstrip() y strip() para eliminar los espacios y mostrar el resultado.
- 2.8 Crea una variable con el nombre de un archivo que incluya una extensión (por ejemplo, 'notas_python.txt'). Usa el método removesuffix() para mostrar el nombre del archivo sin la extensión.

## Tipo de dato: Números enteros (Integers) y números de punto flotante (Floats)

Los números enteros (integers) son aquellos que no tienen parte decimal, mientras que los números de punto flotante (floats) son aquellos que sí tienen una parte decimal. En Python, ambos tipos de datos se pueden manipular utilizando operadores aritméticos básicos como suma (+), resta (-), multiplicación (*), división (/), división entera (//), módulo (%) y potencia (**).

### Ejemplos de operaciones:
- Suma: 2 + 2
- Resta: 2 - 5
- Multiplicación: 5 * 9
- División: 6 / 2
- División entera: 7 // 2
- Exponenciación: 3 ** 4

Una de las cosas que hay que tomar en cuenta es el orden de prioridad en las operaciones matemáticas. Python se alinea con el acrónimo PEMDAS, que representa: Paréntesis, Exponenciación, multiplicación, división, adición y sustracción. Recuerda que en caso de encontrase 2 operaciones iguales se evalúa primero barriendo la operación completa desde la izquierda.

También se pueden convertir entre estos dos tipos de datos utilizando las funciones integradas `int()` y `float()`. Por ejemplo, `int(3.7)` devolverá `3`, mientras que `float(5)` devolverá `5.0`.

Se explica un truco para tener mejor legibilidad al trabajar con números grandes, que es usar guiones bajos (_) para separar los dígitos. Por ejemplo, en lugar de escribir `1000000`, se puede escribir `1_000_000`, lo que hace que sea más fácil de leer.

### Asignación múltiple

Python tiene algo muy útil y es el 'desempaquetado de iterables', con él, podemos hacer cosas grandiosas como hacer el cambio de variables. Por ejemplo:

```python
x , y = y , x

# O también
x , y, z = 0, 1 , 2
```
Aquí lo que pasa por detrás de estas expresiones es un proceso de 3 pasos:

1. Evaluación de la Derecha:

Antes de asignar nada, Python evalúa todo lo que está a la derecha del signo "=". En el caso de 0, 0, 0, aunque no veas paréntesis, Python lo interpreta como una tupla. En memoria, se crea temporalmente un objeto contenedor (una tupla) que contiene los tres valores: (0, 1, 2).

2. El Desempaquetado (Unpacking):

Una vez que la tupla está lista, Python mira cuántas "etiquetas" (variables) hay a la izquierda. El intérprete extrae los elementos de la tupla uno por uno siguiendo el orden de izquierda a derecha. El primer 0 se prepara para x, el segundo número para y, y el tercero para z.

3. Asignación Atómica:

Finalmente, se realizan las asignaciones de los nombres a las direcciones de memoria de esos valores.

Otra cosa interesante es que Python por defecto no maneja el concepto de CONSTANTES. De hecho, se recurre a una convención para escribir una variable que debería comportarse y manejarse como constante pero no está sujeta a evaluación por parte del interprete de Python. 

Imaginemos que tenemos un máximo de intentos antes de que se bloquee la cuenta dentro de un login. Podríamos tener una constante tal que:

```python
MAX_ATTEMPS = 3
```

Por último, tenemos los comentarios que son notaciones valiosas que podemos dejar en nuestro código para dejarlo lo más comentado posible. Hay algo que existe dentro de la comunidad de Python que se llama: "Zen de Python". Esto es un conjunto de pensamientos y filosofía dentro del lenguaje que terminan siendo las buenas prácticas del lenguaje. Como por ejemplo: el código debe ser lo más limpio y autodocumentado posible pero en situaciones nuestra solución podría no entenderse al 100% todo el tiempo y allí en donde los comentarios brillan, ya que son un soporte más para el trabajo colaborativo.

Para comentar el código basta con escribir "#" y seguido de este símbolo, la nota que queremos dejar.

```python
# Este es un comentario
print('Arriba hay un comentario aunque no lo ves')
```

Cabe destacar que los comentarios no se ven cuando se ejecuta el código, simplemente son notaciones dentro de nuestro editor de código.

*Ejercicios propuestos*:
- 2-9. *Number whatever:* Consigue el mismo resultado empleando las distintas operaciones aritméticas usando Python. Procura que el resultado en la terminal tenga el mismo número tantas veces como operaciones distintas hayas hecho.
- 2-10. *Numero de la suerte:* Crea una variable que represente el número de la suerte y muéstralo en pantalla.
- 2-11.*Agrega comentario:* Agrega comentarios a los 2 programas que has hecho en la parte matemática.
- 2-12.*Culebra Zen:* Crea un archivo nuevo e importa el zen de python para que sea mostrado en consola. Importa la librería "this"   
