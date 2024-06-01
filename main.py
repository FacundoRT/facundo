import pygame
import random
import tkinter as tk
from tkinter import messagebox

# Función para dibujar la serpiente en la pantalla
def nuestra_viborita(bloque_vibora, lista_vibora, dis):
    for x in lista_vibora:
        pygame.draw.rect(dis, (255, 255, 0), [x[0], x[1], bloque_vibora, bloque_vibora])  # Viborita amarilla

# Función para mostrar la puntuación en la pantalla
def tu_puntuacion(puntuacion, dis, fuente_puntuacion):
    valor = fuente_puntuacion.render("Tu Puntuación: " + str(puntuacion), True, (255, 255, 102))
    dis.blit(valor, [0, 0])

# Función para mostrar mensajes en la pantalla
def mensaje(msg, color, dis, estilo_fuente, ancho_dis, alto_dis, y_desplazamiento=0):
    mesg = estilo_fuente.render(msg, True, color)
    dis.blit(mesg, [ancho_dis / 6, alto_dis / 3 + y_desplazamiento])

# Función principal que ejecuta el juego
def bucle_juego():
    pygame.init()
    ancho_dis = 800
    alto_dis = 600
    dis = pygame.display.set_mode((ancho_dis, alto_dis))
    pygame.display.set_caption('Juego de la Viborita')

    reloj = pygame.time.Clock()
    bloque_vibora = 10
    velocidad_vibora = 15

    estilo_fuente = pygame.font.SysFont("bahnschrift", 25)
    fuente_puntuacion = pygame.font.SysFont("comicsansms", 35)

    juego_terminado = False
    juego_cerrado = False

    x1 = ancho_dis / 2
    y1 = alto_dis / 2

    cambio_x1 = 0
    cambio_y1 = 0

    lista_vibora = []
    longitud_vibora = 1

    comida_x = round(random.randrange(0, ancho_dis - bloque_vibora) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto_dis - bloque_vibora) / 10.0) * 10.0

    while not juego_terminado:

        while juego_cerrado == True:
            dis.fill((0, 128, 0))  # Fondo verde
            mensaje("¡Perdiste! Presiona Q para salir o C para jugar de nuevo", (213, 50, 80), dis, estilo_fuente, ancho_dis, alto_dis)
            tu_puntuacion(longitud_vibora - 1, dis, fuente_puntuacion)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        juego_terminado = True
                        juego_cerrado = False
                    if event.key == pygame.K_c:
                        bucle_juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_terminado = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cambio_x1 = -bloque_vibora
                    cambio_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    cambio_x1 = bloque_vibora
                    cambio_y1 = 0
                elif event.key == pygame.K_UP:
                    cambio_y1 = -bloque_vibora
                    cambio_x1 = 0
                elif event.key == pygame.K_DOWN:
                    cambio_y1 = bloque_vibora
                    cambio_x1 = 0

        if x1 >= ancho_dis or x1 < 0 or y1 >= alto_dis or y1 < 0:
            juego_cerrado = True
        x1 += cambio_x1
        y1 += cambio_y1
        dis.fill((0, 128, 0))  # Fondo verde
        pygame.draw.rect(dis, (255, 0, 0), [comida_x, comida_y, bloque_vibora, bloque_vibora])  # Manzana roja
        cabeza_vibora = []
        cabeza_vibora.append(x1)
        cabeza_vibora.append(y1)
        lista_vibora.append(cabeza_vibora)
        if len(lista_vibora) > longitud_vibora:
            del lista_vibora[0]

        for x in lista_vibora[:-1]:
            if x == cabeza_vibora:
                juego_cerrado = True

        nuestra_viborita(bloque_vibora, lista_vibora, dis)
        tu_puntuacion(longitud_vibora - 1, dis, fuente_puntuacion)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho_dis - bloque_vibora) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto_dis - bloque_vibora) / 10.0) * 10.0
            longitud_vibora += 1

        reloj.tick(velocidad_vibora)

    pygame.quit()
    quit()

# Función para iniciar el juego
def iniciar_juego():
    root.destroy()
    bucle_juego()

# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    messagebox.showinfo("Instrucciones", 
                        "Bienvenido al Juego de la Viborita.\n"
                        "El objetivo es comer la mayor cantidad de comida posible.\n"
                        "Cada vez que comas, la viborita crecerá.\n"
                        "¡No choques con los bordes ni contigo mismo!\n"
                        "Presiona las teclas de flechas para moverte.\n"
                        "Presiona Q para salir o C para jugar de nuevo cuando pierdas.")

# Crear la ventana de tkinter para la pantalla de inicio
root = tk.Tk()
root.title("Juego de la Viborita")

# Configuración de la ventana de inicio
canvas = tk.Canvas(root, width=800, height=600, bg="blue")
canvas.pack()

texto_bienvenida = canvas.create_text(400, 200, text="Juego de la Viborita", fill="white", font=("bahnschrift", 35))
boton_instrucciones = tk.Button(root, text="Instrucciones", command=mostrar_instrucciones)
boton_iniciar = tk.Button(root, text="Iniciar Juego", command=iniciar_juego)
ventana_boton_instrucciones = canvas.create_window(400, 300, anchor="n", window=boton_instrucciones)
ventana_boton_iniciar = canvas.create_window(400, 350, anchor="n", window=boton_iniciar)

root.mainloop()




