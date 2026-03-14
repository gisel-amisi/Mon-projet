import pygame
import random

pygame.init()
pygame.mixer.init()
SCREEN_WIDHT = 800
SCREEN_HEIHT = 600
screen = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIHT))
pygame.display.set_caption("Devine le mot")

font = pygame.font.SysFont(None,50)
small_font = pygame.font.SysFont(None,35)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Images
background = pygame.image.load("asset/assis.jpg")
background = pygame.transform.scale(background,(SCREEN_WIDHT,SCREEN_HEIHT))

background_win = pygame.image.load("asset/OIP.jpeg")
background_win =  pygame.transform.scale(background,(SCREEN_WIDHT,SCREEN_HEIHT))

#Sons
pygame.mixer.music.load("asset/Exploration Theme.ogg")
pygame.mixer.music.play(-1)

gameover_sound = pygame.mixer.Sound("asset/GameOver.wav")
win_sound = pygame.mixer.Sound("asset/mrstokes302-you-win-sfx-442128.mp3")

#Mot par niveau
word_level  = {
    1: [{"mot": "CHIEN", "indice":"Animal domestique"},
        {"mot": "MER", "indice":"Etendu d'eau salé"}],
    2: [{"mot": "LUNE", "indice":"Astre"},
        {"mot": "MONTAGNE", "indice":"importante élévation de terrain"}],
    3: [{"mot": "ELEPHANT", "indice":"Animal sauvage à trompe"},
        {"mot": "PYTHON", "indice":"Langage de programmation"}],
    4: [{"mot": "POMME", "indice":"Fruit"},
        {"mot": "SOLEIL", "indice":"Etoile"}],
    5: [{"mot": "VOIURE", "indice":"Moyen de transport"},
        {"mot": "FOOTBALL", "indice":"Sport"}],
}
def nouveau_mot(level):
    if len(word_level [level]) == 0:
        return None, None, None
    mot_choisi = random.choice(word_level[level])

    word_level[level].remove(mot_choisi)
    mot = mot_choisi["mot"]
    indice = mot_choisi["indice"]
    affichage = ["_"]  *len (mot)
    return mot, indice, affichage

level = 1
mot, indice, affichage = nouveau_mot(level)
attempts = 0
max_attempts = 5
score = 0
game_over = False
win_screen = False

def draw_text(text, font, color, x, y):
    img = font.render (text, True, color,)
    screen.blit(img, (x,y))

running = True
while running:
     if win_screen:
         screen.blit(background_win,(0,0))
     else:
         screen.blit(background, (0,0))
     if game_over:
         draw_text("GAME OVER",font, RED, 320, 200)
         draw_text("ESPACE pour niveau suivant", small_font, WHITE, 220, 400)
     elif win_screen:
         draw_text("Félicitation!", font, GREEN, 320, 200)
         draw_text("ESPACE pour niveau suivant", small_font, WHITE, 220, 400)
     else:
         draw_text(" ".join(affichage), font, WHITE, 100, 300)
         draw_text("Indice: " + indice, small_font, WHITE, 100, 300)
         draw_text(f"Erreur: {attempts}/{max_attempts}", small_font, RED, 100, 350)
         draw_text(f"Score: {score}", small_font, WHITE, 100, 400)
         draw_text(f"Niveau: {level}", small_font, WHITE, 100, 450)

     pygame.display.flip()

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         elif event.type == pygame.KEYDOWN:
             if not game_over and not win_screen:
                 lettre = event.unicode.upper()
                 if lettre in mot:
                     for i in range(len(mot)):
                         if mot[i] == lettre:
                             affichage[i] = lettre
                 else:
                     attempts +=1

             elif game_over and event.key == pygame.K_SPACE:
                 level = 1
                 score = 0
                 mot, indice, affichage = nouveau_mot(level)
                 attempts =0
                 game_over = False

             elif win_screen and event.key == pygame.K_SPACE:
                 level +=1
                 if level > 6:
                     level = 1
                 mot, indice, affichage = nouveau_mot(level)
                 attempts = 0
                 win_screen = False
     if not game_over and not win_screen and "_" not in affichage:
         score += 1
         win_sound.play()
         win_screen = True
     if not game_over and not win_screen and attempts >= max_attempts:
         gameover_sound.play()
         game_over = True

pygame.quit()

                 

         
         
