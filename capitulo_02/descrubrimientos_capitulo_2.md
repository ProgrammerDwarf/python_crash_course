# Descubrimientos durante la realización de ejercicios

1. Los métodos usados en este capítulo sobre cadenas de texto no cambian dicha cadena de manera definitiva.
2. Existen otros elementos considerados "whitespaces" como \f y \v, el primero es un salto de página y el segundo es una tabulación vertical.
3. Dentro del Zen de Python se menciona algo llamado "Namespaces" y al averiguar de qué se trata es, practicamente, una invitación a ser explícito con las declaraciones que se usan, incluso en los paquetes. Me explico: Puede ocurrir que 2 librerías tengan el mismo nombre para un método o función, por lo que para evitar esto se crean estos Namespaces que es declarar a qué librería o paquete pertenece esa librería:
 ```Python
 import math
import my_custom_math

# Aquí no hay confusión gracias a los namespaces 'math' y 'my_custom_math'
print(math.sqrt(16)) 
print(my_custom_math.sqrt(16))
```