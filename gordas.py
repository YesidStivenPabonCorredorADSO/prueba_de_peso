import cv2
import pygame
import numpy as np

# Inicializar Pygame
pygame.init()

# Pedir el peso al usuario
peso = float(input("Ingrese su peso: "))

# Comprobar si el peso supera los 100 kg
if peso > 100:
    # Inicializar el mezclador de sonido
    pygame.mixer.init()

    # Cargar y reproducir música
    pygame.mixer.music.load("oye-gela-escuchate-esto-saturado.mp3")  # Reemplaza 'music.mp3' con el nombre de tu archivo de música
    pygame.mixer.music.play(-1)  # El argumento -1 hace que la música se reproduzca en bucle

    # Cargar la imagen
    imagen = cv2.imread('12482.jpg')  # Reemplaza '12482.jpg' con la ruta de tu imagen

    # Verificar si la imagen se cargó correctamente
    if imagen is None:
        print("Error: No se pudo cargar la imagen.")
    else:
        # Convertir la imagen de BGR a RGB para que sea compatible con Pygame
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # Convertir la imagen a formato compatible con Pygame
        imagen_pygame = pygame.surfarray.make_surface(np.rot90(imagen))

        # Crear una ventana de Pygame
        pantalla = pygame.display.set_mode((imagen.shape[1], imagen.shape[0]))

        # Bucle principal de Pygame
        ejecutando = True
        angulo = 0

        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False

            # Rotar la imagen
            imagen_rotada = pygame.transform.rotate(imagen_pygame, angulo)
            angulo += 1

            # Centrar la imagen en la pantalla
            rect = imagen_rotada.get_rect(center=(pantalla.get_width()//2, pantalla.get_height()//2))

            # Limpiar la pantalla antes de dibujar la nueva imagen
            pantalla.fill((0, 0, 0))

            # Dibujar la imagen rotada
            pantalla.blit(imagen_rotada, rect)

            # Actualizar la pantalla
            pygame.display.flip()

        # Detener la música y cerrar Pygame
        pygame.mixer.music.stop()
        pygame.quit()
else:
    print("Tu peso no supera los 100 kg.")
