import sys
import os
import math
import pygame
pygame.init()
folder = "musics"
every_sing = [song for song in os.listdir(folder) if song.endswith(".mp3")]
c_song_index = 0
screen = pygame.display.set_mode((400, 400))

def plays(index):
    pygame.mixer.init()
    file_path = os.path.join(folder, every_sing[index])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

plays(c_song_index)

while True:
    print(" p - pause, r - resume")
    print("n - next, b - back(previous)")
    print(" e - exit")
    query = input(" ")

    if query == "p":
     pygame.mixer.music.pause()
     print("pause")
    elif query == "r":
     pygame.mixer.music.unpause()
     print("resume")
    elif query == "n":
     c_song_index = (c_song_index + 1) % len(every_sing)
     plays(c_song_index)
     print("pause")
    elif query == "b":
     c_song_index = (c_song_index + 1) % len(every_sing)
     plays(c_song_index)
    elif query == "e":
      pygame.quit()

while True:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()