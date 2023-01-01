import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('lovers.mp3')
pygame.mixer.music.play()
input("\nPress any Key to Stop Music or Exit")
pygame.event.wait()
pygame.mixer.music.stop()
print("\nPlay Stopped or Exit")
