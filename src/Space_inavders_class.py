import pygame
class root:
    def __init__(self,file,width,height,x=0,y=50 ):
        self.image_root = pygame.image.load(file)
        self.image_root = pygame.transform.scale(self.image_root, (width,height))
        self.root_rect = self.image_root.get_rect(topleft = (x, y))

class Player:
    def __init__(self,file,x = 750 // 2,y = 750 - 30,width = 70,height = 70,speed = 6):
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, (width,height))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
        self.height=height
        self.player_life = True


class player_gun:
    def __init__(self, x , y , width = 8, height=15, speed = [6,12]):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x + 22 , y - 10, width, height)
        self.speed = speed
        


class Cuore:
    def __init__(self,x,y,image = 'assets/images/CUORE_VERO.png',width = 25, height = 25):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width,height))
        self.life = True



class aliens:
    def __init__(self, x, y, file1,file2, width=50, height=50, speed=[1,10]):
        self.image1 = pygame.image.load(file1)
        self.image2 = pygame.image.load(file2)
        self.image1 = pygame.transform.scale(self.image1, (width, height))
        self.image2 = pygame.transform.scale(self.image2, (width, height))
        self.rect = self.image1.get_rect(topleft=(x, y))
        self.rect = self.image2.get_rect(topleft=(x, y))
        self.speed = speed
        self.still_live = True
    
    
        

class aliens_gun:
    def __init__(self, x , y, width=5, height=15, speed=[1, 10]):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.alien_shot = False

class Vierecke:
    def __init__(self,x,y,width = 10,height = 10):
        self.rect= pygame.Rect(x - 10,y + 22,width,height)
        self.width = width
        self.height = height
        self.vierecke_life = True