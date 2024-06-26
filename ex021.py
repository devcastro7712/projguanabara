#Faça um programa em python que abra e reproduza um áudio de um arquivo mp3
import pygame

while 1 == 1:
    pygame.init()
    pygame.mixer.music.load("ex021.mp3.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()