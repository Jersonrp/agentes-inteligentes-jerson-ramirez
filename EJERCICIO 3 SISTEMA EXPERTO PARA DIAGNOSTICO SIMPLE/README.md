Este sistema experto realiza diagnósticos básicos basados en los síntomas ingresados por el usuario. Utiliza condicionales para comparar los síntomas introducidos y generar un diagnóstico preliminar, sugiriendo posibles condiciones médicas o recomendaciones generales.

Cómo Funciona
Ingreso de Síntomas: El sistema solicita al usuario que ingrese si tiene ciertos síntomas comunes. Los síntomas solicitados son:

Tos
Fiebre
Dolor de cabeza
Cansancio
Dolor de garganta
El usuario debe responder con "sí" o "no" a cada pregunta.

Evaluación de Síntomas: El sistema evalúa los síntomas ingresados utilizando condicionales (if, elif, else). Según las combinaciones de síntomas, se genera un diagnóstico basado en las siguientes reglas:

Si el usuario tiene tos, fiebre y dolor de cabeza, se sugiere una gripe o resfriado.
Si tiene tos, fiebre y dolor de garganta, se sugiere una infección viral.
Si tiene fiebre, dolor de cabeza y cansancio, se indica un posible cuadro de fatiga general o gripe.
Y otras combinaciones de síntomas también desencadenan diagnósticos específicos.
Generación del Diagnóstico: Según los síntomas ingresados, el sistema muestra un mensaje con el diagnóstico correspondiente. Si no se encuentran combinaciones preocupantes de síntomas, el sistema sugiere que el usuario consulte a un medico para una mejor evaluacion.
