Imagina que eres el operador de un semáforo en una intersección muy transitada. Tu trabajo es observar cuántos autos están esperando y decidir cuánto tiempo debe durar cada luz para que el tráfico fluya de la mejor manera posible.

Ahora bien, en lugar de que tú estés parado ahí todo el día tomando decisiones, hemos creado un agente inteligente que hace este trabajo por ti.

EL AGENTE EN EL CODIGO FUNCIONA DE LA SIGUIENTE MANERA
Observa el tráfico

El agente usa un sensor simulado con random.randint(0, 15) para contar cuántos carros están esperando.
Si hay muchos carros, significa que la calle está congestionada. Si hay pocos, el tráfico es ligero.
Decide cuánto tiempo dura cada luz

Si hay muchos carros (más de 10): entra a la primer condicional que cada color del semaforo tiene estipulado mas tiempos
Mantiene la luz verde encendida más tiempo para dejar pasar más vehículos.
La luz roja dura más también para evitar colapsos en la otra vía.
Si hay tráfico moderado (entre 5 y 10 autos): el codigo ejecuta la segunda condicional
Da tiempos intermedios para equilibrar el paso.
Si hay pocos autos (menos de 5):
Cambia más rápido entre luces para evitar que los conductores esperen sin necesidad.
Actúa en consecuencia

Muestra en pantalla cuál es el estado del semáforo y cuánto tiempo durará.
Usa time.sleep() para simular el paso del tiempo en cada color.
Luego vuelve a empezar, detectando otra vez el tráfico y ajustando los tiempos.
