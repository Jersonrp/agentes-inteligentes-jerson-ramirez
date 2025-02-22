import random

def recomendar_pelicula():
   
    peliculas = {
        "acción": ["Misión Rescate 2", "Mercenarios", "Rápido y Furioso", "13 Horas: Los Soldados Secretos de Bengasi"],
        "comedia": ["Esposa de Mentira", "Un Espía y Medio", "Policías del Desorden", "Son Como Niños 2"],
        "ciencia ficción": ["Jumanji", "Tierra Errante", "Legión de Ángeles", "Destino de Júpiter"],
        "romántica": ["Stand de los Besos", "Votos de Amor", "Cuestión de Tiempo", "Lo Mejor de Mi"]
    }

    while True:
       
        genero_favorito = input("¿Cuál es tu género favorito de película? (acción, comedia, ciencia ficción, romántica): ").strip().lower()

       
        if genero_favorito in peliculas:
           
            pelicula_recomendada = random.choice(peliculas[genero_favorito])
            print(f"Te recomendamos ver: {pelicula_recomendada}")
            
            
            otra_recomendacion = input("¿Quieres otra recomendación? (sí/no): ").strip().lower()
            if otra_recomendacion != "sí":
                print("Gracias por utilizar el asistente de recomendación de películas. ¡Hasta pronto!")
                break
        else:
            print("Lo siento, no tenemos recomendaciones para ese género. Por favor elige uno de los siguientes: acción, comedia, ciencia ficción, romántica.")


recomendar_pelicula()
