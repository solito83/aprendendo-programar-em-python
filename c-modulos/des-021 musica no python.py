des = 'Música no python'
print('{}'.format(des))
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer('pushme.mp3')
