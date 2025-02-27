import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
font = pygame.font.Font(None, 36)
text = ""
list_text = []
list_text.append(text)
pygame.key.start_text_input()  # Inizia l'input di testo

running = True
while running:
    screen.fill((30, 30, 30))  # Sfondo scuro
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.TEXTINPUT:  # Evento di input testo
            text += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                text += " "
            if event.key == pygame.K_BACKSPACE:  # Cancella carattere
                text = text[:-1]
        print (text)
        
        print (list_text)

        

    render_text = font.render(text, True, (255, 255, 255))
    screen.blit(render_text, (20, 100))

    pygame.display.flip()

pygame.key.stop_text_input()  # Ferma l'input di testo
pygame.quit()