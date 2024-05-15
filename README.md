# tp3
## 1a
Con hilos se ejecuta aproximadamente en un promedio de 10 veces un segundo mas rapido. debido a la forma en que se gestionan las tareas y los recursos del sistema(sin hilos se ejecuta de manera secuencial). Al usar hilos, podes ejecutar distintas tareas de manera simultánea, lo que permite que partes del programa se desarrollen de forma independiente. Esto optimiza el uso de los recursos del sistema, potencialmente mejorando su eficiencia.

## 1b 
comparando con otro estudiante, el tuvo con hilos 4,01460 mientras que yo tuve 4.05920 y sin hilos tuvo 5.13283 y yo tuve 5.23259.

## 1c
Después de hacer esos cambios, noté que el programa tardaba más en completarse. ¿Por que esto? Resulta que al agregar esas líneas, incluí dos bucles que no eran realmente necesarios. Estos bucles solo hacían que el programa se detuviera por un tiempo corto, sin hacer algo útil.
Estos bucles estaban dentro de las partes del programa llamadas "sumador" y "restador", y cada uno se ejecutaba mil veces. Aunque cada vez que el bucle se repetía no contribuía en gran medida al resultado final, sí añadía tiempo extra al proceso tota,en resumen, el programa tardaba más en completarse porque introduje estas acciones adicionales. Además, en cuanto al cambio en el valor final, esto ocurrió debido a este tiempo adicional. Al agregar los bucles extras, prolongué el tiempo en el que el programa estaba realizando cálculos innecesarios. Esto afectó cómo el programa modificaba su resultado final.

## 2a 
<a href="./tp3/con_race_condition_corregido.c">puzzle corregido</a>

## 2b
![2 comenzales 8 hamburguesas](![untitled (4) (1)](https://github.com/santucho12/ASO2024TPs/assets/166550221/4d2474b7-cf57-4575-9953-0589fc43252d)
)
