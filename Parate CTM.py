import os
import random
import time

path = "D:\Música"  # Reemplaza "TuUsuario" con tu nombre de usuario en Windows
song_list = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]
active = True

# Esperar 45 minutos antes de comenzar el temporizador
time.sleep(45*60)

while active:
    song = random.choice(song_list)
    time.sleep(5)  # Agregar un retraso de 5 segundos para evitar que se interrumpa la reproducción de la canción anterior
    os.startfile(song)
    stop = input("¿Deseas detener el temporizador? (si/no): ")
    if stop.lower() == "si":
        active = False
    else:
        time.sleep(45*60)
