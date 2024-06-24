import pygame
from ClassInterface import * 


pygame.init()

pygame.display.set_caption("Test affichage")
windowsSurface = pygame.display.set_mode([800,640])

#Fonction 
def sizeTexte(text):
    textHeight , textWithd = text.get_size()
    return textHeight ,textWithd 



#colors

Blue = newColors('Blue',(0,0,255))
Black = newColors('Black',(0,0,0))
White = newColors('White',(255,255,255))
Red = newColors('Red',(255,0,0))
Yellow = newColors('Yellow',(255,255,0))
Green = newColors('Green',(14,104,0))
Magenta = newColors('Magenta',(109,0,101))

#Class
PlayButton = NewRect('PlayButton',260,220,Colors['Green'],windowsSurface,50,200)
SettingButton = NewRect('SettingButton',260,270,Colors['Magenta'],windowsSurface,50,200)
DificultyButton = NewRect('DificultyButton',260,220,Colors['Magenta'],windowsSurface,50,200)
BackButton = NewRect('BackButton',260,270,Colors['Red'],windowsSurface,50,200)
EasyButton = NewRect('EasyButton',260,220,Colors['Green'],windowsSurface,50,200)
MediumButton = NewRect('MediumButton',260,270,Colors['Yellow'],windowsSurface,50,200)
HardButton = NewRect('HardButton',260,320,Colors['Red'],windowsSurface,50,200)

#hitboxbutton
hitboxPlayButton = PlayButton.hitbox()

hitboxSettingButton = SettingButton.hitbox()

hitboxDificultyButton = DificultyButton.hitbox()

hitboxBackButtonButton = BackButton.hitbox()

hitboxEasyButton = EasyButton.hitbox()

hitboxMediumButton = MediumButton.hitbox()

hitboxHardButton = HardButton.hitbox()

#hitboxEasyButton





#texte 
Cakecafe_font = pygame.font.Font('Cakecafe.ttf', 20)

PlayButtonTexte = Cakecafe_font.render("Play", True,Colors['White'])

SettingTexte = Cakecafe_font.render("Setting", True,Colors['White'])

DificultyTexte = Cakecafe_font.render("Dificulty",True,Colors['White'])

BackTexte = Cakecafe_font.render('Back',True,Colors['White'])

EasyTexte = Cakecafe_font.render('Easy',True,Colors['Black'])

MediumTexte = Cakecafe_font.render('Medium',True,Colors['Black'])

HardTexte = Cakecafe_font.render('hard',True,Colors['Black'])



#Rectangle souris
mouseX = 0
mouseY = 0
mouseRect = pygame.Rect(mouseX,mouseY,100,100)


launched = True 


while launched :
    windowsSurface.fill(Colors['Black'])
    PlayButton.place()
    PlayButton.hitbox()
    windowsSurface.blit(PlayButtonTexte, (PlayButton.midButton(sizeTexte(PlayButtonTexte)[0],sizeTexte(PlayButtonTexte)[1]),PlayButton.midButton(sizeTexte(PlayButtonTexte)[0],sizeTexte(PlayButtonTexte)[1])))

    hitboxSettingButton
    SettingButton.place()
    pygame.draw.rect(windowsSurface,Colors['Black'],mouseRect)
    windowsSurface.blit(SettingTexte, (SettingButton.midButton(sizeTexte(SettingTexte)[0],sizeTexte(SettingTexte)[1]),SettingButton.midButton(sizeTexte(SettingTexte)[0],sizeTexte(SettingTexte)[1])))
    pygame.display.flip()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            launched = False
        
        if event.type == pygame.MOUSEMOTION:
            mouseRect = pygame.Rect(event.pos[0],event.pos[1],1,1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :
                if mouseRect.colliderect(hitboxPlayButton):
                    print("Le jeux se lance...")
                if mouseRect.colliderect(hitboxSettingButton):
                    #print("Je suis presser")
                    SettingButtonPressed = True 
                    windowsSurface.fill(Colors['Black'])
                    DificultyButton.place()
                    hitboxDificultyButton
                    windowsSurface.blit(DificultyTexte, (DificultyButton.midButton(sizeTexte(DificultyTexte)[0],sizeTexte(DificultyTexte)[1]),DificultyButton.midButton(sizeTexte(DificultyTexte)[0],sizeTexte(DificultyTexte)[1])))
                    pygame.display.flip()
                    while SettingButtonPressed :
                        BackButton.place()
                        DificultyButton.place()
                        hitboxDificultyButton
                        hitboxBackButtonButton
                        windowsSurface.blit(BackTexte, (BackButton.midButton(sizeTexte(BackTexte)[0],sizeTexte(BackTexte)[1]),BackButton.midButton(sizeTexte(BackTexte)[0],sizeTexte(BackTexte)[1])))
                        windowsSurface.blit(DificultyTexte, (DificultyButton.midButton(sizeTexte(DificultyTexte)[0],sizeTexte(DificultyTexte)[1]),DificultyButton.midButton(sizeTexte(DificultyTexte)[0],sizeTexte(DificultyTexte)[1])))
                        hitboxDificultyButton
                        pygame.display.flip()
                        pygame.draw.rect(windowsSurface,Colors['Black'],mouseRect)
                        for events in pygame.event.get():
                            if events.type == pygame.QUIT :
                                launched = False
                                SettingButtonPressed = False
                            if events.type == pygame.MOUSEMOTION:
                                mouseRect = pygame.Rect(events.pos[0],events.pos[1],1,1)

                            if events.type == pygame.MOUSEBUTTONDOWN:
                                if events.button == 1 :
                                    if mouseRect.colliderect(hitboxDificultyButton):
                                        #print("Je suis un bouton pour entrer dans le choix des dificultés")
                                        windowsSurface.fill(Colors['Black'])
                                        DificultyButtonPressed = True
                                        while DificultyButtonPressed :
                                                for event in pygame.event.get() :
                                                    if event.type == pygame.QUIT :
                                                        launched = False
                                                        SettingButtonPressed = False
                                                        DificultyButtonPressed = False
                                                    if event.type == pygame.MOUSEMOTION :
                                                        mouseRect = pygame.Rect(events.pos[0],events.pos[1],1,1)
                                                    if event.type == pygame.MOUSEBUTTONDOWN :
                                                        if event.button == 1 :
                                                            if mouseRect.colliderect(hitboxEasyButton) : 
                                                                print("Vous êtes en dificulter simple")
                                                                DificultyButtonPressed = False
                                                            if mouseRect.colliderect(hitboxMediumButton) :
                                                                print("Vous êtes en difficulter moyenne")
                                                                DificultyButtonPressed = False
                                                            if mouseRect.colliderect(hitboxHardButton) :
                                                                print("Vous êtes en dificulter Dificile")
                                                                DificultyButtonPressed = False
                        
                                                windowsSurface.fill(Colors['Black'])
                                                EasyButton.place()
                                                windowsSurface.blit(EasyTexte, (EasyButton.midButton(sizeTexte(EasyTexte)[0],sizeTexte(EasyTexte)[1]),EasyButton.midButton(sizeTexte(EasyTexte)[0],sizeTexte(EasyTexte)[1])))
                                                MediumButton.place()
                                                windowsSurface.blit(MediumTexte, (MediumButton.midButton(sizeTexte(MediumTexte)[0],sizeTexte(MediumTexte)[1]),MediumButton.midButton(sizeTexte(MediumTexte)[0],sizeTexte(MediumTexte)[1])))
                                                HardButton.place()
                                                windowsSurface.blit(HardTexte, (HardButton.midButton(sizeTexte(HardTexte)[0],sizeTexte(HardTexte)[1]),HardButton.midButton(sizeTexte(HardTexte)[0],sizeTexte(HardTexte)[1])))
                                                pygame.display.flip()
                                                            
                                    if mouseRect.colliderect(hitboxBackButtonButton) : 
                                        print("Vous sorter des parametre")
                                        SettingButtonPressed = False
                        
                        windowsSurface.fill(Colors['Black'])
                        BackButton.place()      
                        DificultyButton.place()
                        hitboxDificultyButton
                        hitboxBackButtonButton
                        windowsSurface.blit(DificultyTexte, (DificultyButton.midButton(sizeTexte(DificultyTexte)[0],sizeTexte(DificultyTexte)[1]),DificultyButton.midButton(sizeTexte(DificultyTexte)[0],sizeTexte(DificultyTexte)[1])))
                        pygame.draw.rect(windowsSurface,Colors['Black'],mouseRect)
                        windowsSurface.blit(BackTexte, (BackButton.midButton(sizeTexte(BackTexte)[0],sizeTexte(BackTexte)[1]),BackButton.midButton(sizeTexte(BackTexte)[0],sizeTexte(BackTexte)[1])))
                        hitboxDificultyButton
                        pygame.display.flip()


 


    SettingButton.place()
    pygame.draw.rect(windowsSurface,Colors['Black'],mouseRect)
    windowsSurface.blit(SettingTexte, (SettingButton.midButton(sizeTexte(SettingTexte)[0],sizeTexte(SettingTexte)[1]),SettingButton.midButton(sizeTexte(SettingTexte)[0],sizeTexte(SettingTexte)[1])))
    pygame.display.flip()