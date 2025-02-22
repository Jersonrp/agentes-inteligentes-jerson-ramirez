Este programa es un asistente de recomendación de películas que sugiere títulos basados en el género favorito del usuario. A continuación se explica cómo funciona el flujo del programa:

1. Diccionario de Películas por Género:
   El sistema contiene un diccionario llamado peliculas, que organiza películas en diferentes géneros: acción, comedia, ciencia ficción y romántica. Cada clave del diccionario corresponde a un género, y su valor es una lista de películas recomendadas dentro de ese género.

2. Solicitud de Género:
   El programa solicita al usuario que ingrese su género de película favorito entre las opciones disponibles: acción, comedia, ciencia ficción y romántica.

El programa luego verifica si el género ingresado es válido, es decir, si se encuentra dentro de las claves del diccionario. Si el género no es válido, se muestra un mensaje informando al usuario que debe elegir un género válido.

3. Selección de Película Aleatoria:
   Si el género ingresado es válido, el sistema selecciona una película aleatoria de la lista correspondiente usando la función random.choice(). Esta función elige un elemento de la lista de manera aleatoria.

4. Solicitud de Nueva Recomendación:
   Después de mostrar una película recomendada, el programa pregunta al usuario si desea otra recomendación. Si la respuesta es "sí", el programa vuelve a solicitar un género para hacer una nueva recomendación.

Si la respuesta es "no", el programa imprime un mensaje de despedida y termina.

5. Bucle y Flujo:
   El sistema se ejecuta en un bucle while True que permite que el usuario elija un género y reciba una recomendación. Este bucle continuará hasta que el usuario decida no recibir más recomendaciones.
