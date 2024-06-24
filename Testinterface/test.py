import pygame
pygame.init()
fen = pygame.display.set_mode((800,600))
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
continuer = True
while continuer :
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if evenement.button == 1 :
                fen.fill(BLEU)
                print ("clic bouton gauche")
            if evenement.button == 3 :
                fen.fill(ROUGE)
                print ("clic bouton droit")
            pygame.display.flip()
pygame.display.quit()