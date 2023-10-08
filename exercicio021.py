#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame.mixer
pygame.mixer.init()
musica = pygame.mixer.music.load("/Users/wallessa/PycharmProjects/exercicios_curso_python/Marcha-imperial-star-wars.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): #adicionamos um loop que verifica se a música ainda está tocando usando pygame.mixer.music.get_busy(). O programa só sairá após a música ter terminado de tocar.
    pass
pygame.mixer.quit()


