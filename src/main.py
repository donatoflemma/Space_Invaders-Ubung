import pygame
import random
import json
from pygame import mixer
from Space_inavders_class import *
# mixer init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None )
pygame.init()


root_dimansion = width, height = 750, 750    # 800,600
root_SPACE = root('assets/images/SPACE.jpg',root_dimansion[0],root_dimansion[1] - 50)

black = 0, 0, 0
RED = 255, 0, 0
WHITE = 255, 255, 255
GREEN = 176, 196, 170
root = pygame.display.set_mode(root_dimansion)
# Initial time
start_time = pygame.time.get_ticks()
#Sound track and sound effects
Sound_player=pygame.mixer.Sound("assets/sounds/Player_Sound.mp3")
Sound_schild=pygame.mixer.Sound("assets/sounds/Schild.mp3")
Sound_alien=pygame.mixer.Sound("assets/sounds/Alien_Sound.mp3")
Sound_explosion=pygame.mixer.Sound("assets/sounds/explosion_Alien.mp3")
Sound_gameover=pygame.mixer.Sound("assets/sounds/Game-over.mp3")
Sound_play = pygame.mixer.Sound("assets/sounds/Led Zeppelin - Whole Lotta Love (Official Music Video).mp3")
# we load the font and assign it to the variable fnt
fnt = pygame.font.SysFont("Times New Roman", 24)
Score = 0
#################################### player ###############################################
player = Player('assets/images/navicella_bianca.png')
Gun = player_gun(player.x,player.y)
shot = False
lista_cuore = []
for _ in range (0,3): 
    lista_cuore.append(Cuore(90 - (_ * 25),5))

########################################## ALIENS ###########################################################################################
list_aliens_gun = []
list_aliens = []
Abstand = 20
x_position = (root_dimansion[0] / 2) - ((9 // 2) * (Abstand + 25)) - 100

for i in range(0, 8):
    position = x_position + ((Abstand + 50) * i)
    list_aliens.append(aliens(position, 40, 'assets/images/ALIENO_4.png','assets/images/ALIENO_4_MOVIMENTO.png')) # Navicella 
    list_aliens_gun.append(aliens_gun(position + 23, 70))

for i in range (0,8):
    position = x_position + ((Abstand + 50) * i)
    list_aliens.append(aliens(position,100,'assets/images/ALIENO_3.png','assets/images/ALIENO_3_MOVIMENTO.png')) # Alieno
    list_aliens_gun.append(aliens_gun(position + 23,120))

for i in range (0,8):
    position = x_position + ((Abstand + 50) * i)
    list_aliens.append(aliens(position,160,'assets/images/ALIENO_3.png','assets/images/ALIENO_3_MOVIMENTO.png')) # Alieno
    list_aliens_gun.append(aliens_gun(position + 23,180))

for i in range (0,8):
    position = x_position + ((Abstand + 50) * i)
    list_aliens.append(aliens(position,220,'assets/images/ALIENO_2.png','assets/images/ALIENO_2_MOVIMENTO.png')) # Alieno2
    list_aliens_gun.append(aliens_gun(position + 23,240))

for i in range (0,8):
    position = x_position + ((Abstand + 50) * i)
    list_aliens.append(aliens(position,280,'assets/images/ALIENO_2.png','assets/images/ALIENO_2_MOVIMENTO.png'))  # Alieno2
    list_aliens_gun.append(aliens_gun(position + 23,300 ))

######################################## BLOCK CONSTRUCTION ###################################################         
##############################  the construction goes from bottom to top !!! ######################################### 
Schild_list = []
for i in range (1,7):
    match i :
        case 1 :
            for vierecke in range (0,5):    # 200  205
                for block in range (0,4):   # 67 78 89 100 111 122
                    Schild_list.append(Vierecke((87 + (175 * block)),(height - 108)  - (vierecke * 11)))
        case 2:
            for vierecke in range (0,5):
                for block in range (0,4):
                    Schild_list.append(Vierecke((98 + (175 * block)),(height - 119)  - (vierecke * 11)))
        case 3:
            for vierecke in range (0,5):
               for block in range (0,4):
                    Schild_list.append(Vierecke((109 + (175 * block)),(height - 130)  - (vierecke * 11)))
        case 4:
            for vierecke in range (0,5):
                for block in range (0,4):
                    Schild_list.append(Vierecke((120 + (175 * block)),(height - 130)  - (vierecke * 11)))
        case 5 :
            for vierecke in range (0,5):
                for block in range (0,4):
                    Schild_list.append(Vierecke((131 + (175 * block)),(height - 119)  - (vierecke * 11)))
        case 6:
            for vierecke in range (0,5):
                for block in range (0,4):
                    Schild_list.append(Vierecke((142 + (175 * block)),(height - 108)  - (vierecke * 11)))


###################################### MAIN LOOP ###############################################
lista_provvisoria = []
counter_cuore  = 2
game_over = False
running = True
counter_immagine  = 0
direzione = 1
while running:
    for event in pygame.event.get():
        if running:
            pygame.mixer.Sound.play(Sound_play)
        if event.type == pygame.QUIT:
            running = False

###################################################### ALIEN MOVE #########################################################################
     # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert to seconds
    
    
    if  len(lista_provvisoria) == 0:  # Check for active projectiles
        random_namber = random.randint(0, len(list_aliens) - 1)
        if list_aliens[random_namber].still_live:   
            lista_provvisoria.append(random_namber)
            list_aliens_gun[random_namber].alien_shot = True
            list_aliens_gun[random_namber].rect.y += list_aliens_gun[random_namber].speed[1] 
            pygame.mixer.Sound.play(Sound_alien)
        
            
    elif len(lista_provvisoria) == 1: 
        list_aliens_gun[lista_provvisoria[0]].alien_shot = True
        list_aliens_gun[lista_provvisoria[0]].rect.y += list_aliens_gun[lista_provvisoria[0]].speed[1]
        if list_aliens_gun[lista_provvisoria[0]].rect.y >= height:  # Disable the bullet if it leaves the screen
            list_aliens_gun[lista_provvisoria[0]].alien_shot = False
            list_aliens_gun[lista_provvisoria[0]].rect.y = list_aliens[lista_provvisoria[0]].rect.y
            del lista_provvisoria[0]  

   
################################################ COLLIDERECT - GUN - ALIEN ####################################

    for alien in list_aliens:
        if list_aliens_gun[random_namber].rect.colliderect(alien.rect)  and alien.still_live == True:
            list_aliens_gun[random_namber].alien_shot = False

    for block in Schild_list:
        if list_aliens_gun[random_namber].rect.colliderect(block.rect)  and block.vierecke_life:
            block.vierecke_life = False
            pygame.mixer.Sound.play(Sound_schild)
            list_aliens_gun[random_namber].alien_shot = False  # Disables projectile after hitting a blockade
            list_aliens_gun[random_namber].rect.y = list_aliens[random_namber].rect.y 
            del lista_provvisoria[0]
    
    
        
        if list_aliens_gun[random_namber].rect.colliderect(player.rect):
            lista_cuore[counter_cuore].life = False
            list_aliens_gun[random_namber].alien_shot = False  
            list_aliens_gun[random_namber].rect.y = list_aliens[random_namber].rect.y
            del lista_provvisoria[0] 
            counter_cuore -= 1
        
        for cuore in lista_cuore:
            if  counter_cuore == -1:
                block.vierecke_life = False
                player.player_life = False
                for alien in list_aliens:
                    alien.still_live = False
                for alien_gun in list_aliens_gun:
                    alien_gun.alien_shot = False
                game_over = True
                
                
                
####################################### COLLIDERECT - PLAYER ##########################################################################
        
    
        for block in Schild_list:
            if Gun.rect.colliderect(block.rect) and block.vierecke_life:
                block.vierecke_life = False
                pygame.mixer.Sound.play(Sound_schild)
                shot = False  
                
    
    
        for alien in list_aliens:
            if Gun.rect.colliderect(alien.rect) and alien.still_live:
                alien.still_live = False
                pygame.mixer.Sound.play(Sound_explosion)
                shot = False  
                Score += 10
   
######################################### KEYS ######################################################
        #   KEY_PUSHED ANWENDUNG
    keys_pushed = pygame.key.get_pressed()

    if  keys_pushed[pygame.K_LEFT]: 
        player.rect.x -= player.speed 
         
        
    if  keys_pushed[pygame.K_RIGHT]:  # 
        player.rect.x +=  player.speed
         

    if shot == False:   # I put it here to have it follow the move in time and not to the next frame
            Gun.rect[0] = player.rect.x + 22
            Gun.rect[1] = player.rect.y - 10 


    if keys_pushed[pygame.K_UP] :
        shot = True
        pygame.mixer.Sound.play(Sound_player)
        
    if shot:
        Gun.rect[1] -= Gun.speed[1]

    if  Gun.rect[1] <= 0 : 
        shot = False
     
#             KEY_DOWN
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.QUIT:
            running= False

        if event.key == pygame.K_ESCAPE:
            running= False
    
############################################### Border player ###############################################################################
    if player.rect.left < 0:
        player.rect.left = 0
                           

    if player.rect.right > width:
        player.rect.right = width
#################################################### MOVE ALIEN #########################################################################
    
    for i in range (0,40):
        list_aliens[i].rect[0] = list_aliens[i].rect[0] + list_aliens[i].speed[0]
        list_aliens_gun[i].rect[0] = list_aliens_gun[i].rect[0] + list_aliens_gun[i].speed[0]

        if list_aliens[i].rect.right >= (width - 20) or list_aliens[i].rect.left <= 20 :
            list_aliens[i].speed[0] = - list_aliens[i].speed[0]
            list_aliens_gun[i].speed[0]= - list_aliens_gun[i].speed[0]

            for i in range(0,40): 
                list_aliens[i].rect.y += alien.speed[1] 
                list_aliens_gun[i].rect.y += alien.speed[1]
        
############################################## IN THE ROOT ################################################################################
    
    root.fill(black)    
    root.blit(root_SPACE.image_root,root_SPACE.root_rect)
    if player.player_life == True:
        root.blit(player.image,player)

    for block in Schild_list:
        if block.vierecke_life == True:
            pygame.draw.rect(root,WHITE,block)

  

    for alien_gun in list_aliens_gun:
        if alien_gun.alien_shot == True:
            pygame.draw.rect(root, GREEN, alien_gun)
###################################################CAMBIO IMMAGINE ########################################################
    
    counter_immagine += direzione
    if counter_immagine >= 30:
        direzione = -1
    elif counter_immagine <= 0:
        direzione = 1


    for alien in list_aliens:
        if alien.still_live:  # Check if the alien is alive
            if direzione == 1:
                root.blit(alien.image1, alien.rect)  # Use alien.rect for location
            else:
                root.blit(alien.image2, alien.rect)  
   
    
####################################################################################################################

    for cuore in lista_cuore:
        if cuore.life == True:
            root.blit(cuore.image,(width - cuore.x,cuore.y))

       
    
    time = fnt.render(f"Time: {elapsed_time} sec", True, WHITE)
    surf_text1 = fnt.render(f"SCORE:{Score} ", True, WHITE)          
    surf_text2 = fnt.render(f"LIFE:", True, WHITE)

    root.blit(time, ((width // 3) + 50, 5))
    root.blit(surf_text2, (width - 150, 5))
    root.blit(surf_text1, (10, 5))
    if game_over == True:
        surf_text3 = fnt.render("GAME OVER !!!", True, WHITE)          
        root.blit(surf_text3, (300 , height // 3))
        pygame.mixer.Sound.play(Sound_gameover)

   

    if shot == True:
        pygame.draw.rect(root, GREEN, Gun)
############################################## CLOCK - FLIP - QUIT #################################################################################
   #Set the frame rate i.e. the amount of frames per second, so each time the cycle starts again
    pygame.time.Clock().tick(90)
    pygame.display.flip()   # I always refresh the window and insert updates , important
pygame.mixer.quit()
pygame.quit()