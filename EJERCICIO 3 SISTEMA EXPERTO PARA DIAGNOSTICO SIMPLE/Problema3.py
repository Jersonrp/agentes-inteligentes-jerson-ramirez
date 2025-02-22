def diagnostico():
    print("Bienvenido al sistema de diagnóstico médico básico.")
    
   
    tos = input("¿Tienes tos? (sí/no): ").strip().lower()
    fiebre = input("¿Tienes fiebre? (sí/no): ").strip().lower()
    dolor_cabeza = input("¿Tienes dolor de cabeza? (sí/no): ").strip().lower()
    cansancio = input("¿Te sientes cansado/a? (sí/no): ").strip().lower()
    dolor_garganta = input("¿Tienes dolor de garganta? (sí/no): ").strip().lower()

   
    if tos == 'sí' and fiebre == 'sí' and dolor_cabeza == 'sí':
        print("Diagnóstico: Podrías tener una gripe o resfriado. Te recomendamos descansar e hidratarte bien.")
    elif tos == 'sí' and fiebre == 'sí' and dolor_garganta == 'sí':
        print("Diagnóstico: Podrías tener una infección viral. Si los síntomas persisten, consulta a un médico.")
    elif fiebre == 'sí' and dolor_cabeza == 'sí' and cansancio == 'sí':
        print("Diagnóstico: Podrías estar experimentando un cuadro de fatiga general o gripe.")
    elif tos == 'sí' and dolor_garganta == 'sí':
        print("Diagnóstico: Puede ser un resfriado o faringitis. Considera visitar un médico si los síntomas empeoran.")
    elif cansancio == 'sí' and dolor_cabeza == 'sí':
        print("Diagnóstico: Puede ser agotamiento o estrés. Descansa y mantén una buena hidratación.")
    else:
        print("Diagnóstico: No se encontraron combinaciones preocupantes de síntomas. Si te sientes mal, consulta a un medico para una mejor evaluacion")


diagnostico()
