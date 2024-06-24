import pygame

pygame.init()

def sizeTexte(text):
    textHeight , textWithd = text.get_size()
    return textHeight ,textWithd 


#Colors
Colors = {




}


def newColors(colors,RGB):
    Colors[colors] = RGB




class NewRect():
    def __init__(self,name,coordX,coordY,colors,fenetre,hauteur,largeur):
        self.name = name 
        self.coordX = coordX
        self.coordY = coordY
        self.colors = colors 
        self.fenetre = fenetre
        self.hauteur = hauteur
        self.largeur = largeur
    def place(self):
        name = pygame.Rect(self.coordX,self.coordY,self.largeur,self.hauteur)
        return pygame.draw.rect(self.fenetre,self.colors,name)
    def showCoords(self):
        return self.coordX,self.coordY
    def midButton(self, text_width, text_height):
        midX = self.coordX + (self.largeur // 2) - (text_width // 2)
        midY = self.coordY + (self.hauteur // 2) - (text_height // 2)
        return midX, midY
    def modifyColors(self,newColors):
        self.colors = newColors
        return self.colors
    def modifyCoords(self,X,Y):
        self.coordX = X
        self.coordY = Y 
        return X , Y 
    def hitbox(self) :
        hitbox = pygame.Rect(self.coordX,self.coordY,self.largeur,self.hauteur)
        return pygame.draw.rect(self.fenetre,self.colors,hitbox)
    




#[SCREEN_WIDTH / 2 - text_w / 2, SCREEN_HEIGHT / 2 - text_h / 2])
"""
print(Colors)
newColors('Blue',(0,0,255))
print(Colors)"""