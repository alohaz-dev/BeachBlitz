# imports

import pygame

# vars

# colours

# code


class serverSide():
    def load_window():
        screen = pygame.display.set_mode((750, 500), pygame.RESIZABLE)
        playerPortal.main_portal(screen)

class playerPortal():
    def main_portal(screen):
        while True:
            screen.fill((26, 26, 26))
            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()

class mainMenu():
    def main_menu(screen, session_id):
        while True:
            screen.fill((26, 26, 26))
            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()

class whiteBoard():
    def main_menu():
        screen = pygame.display.set_mode((750, 500), pygame.RESIZABLE)
        while True:
            screen.fill((26, 26, 26))
            pygame.font.init()
            screensize = screen.get_size()
            title_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', screensize[1]//6)
            title_text = title_font.render('beach blitz', True, (229, 229, 229))
            title_rect = title_text.get_rect()
            title_rect.centerx = screensize[0]//2
            title_rect.top = screensize[1]//6

            subtitle_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', screensize[1]//18)
            subtitle = 'developer mode'
            subtitle_color = (255, 226, 96)
            subtitle_text = subtitle_font.render(subtitle, True, subtitle_color)
            subtitle_rect = subtitle_text.get_rect()
            subtitle_rect.centerx = screensize[0]//2
            subtitle_rect.top = title_rect.bottom-10

            screen.blit(title_text, title_rect)
            screen.blit(subtitle_text, subtitle_rect)

            buttonwidth = (screensize[0]-100)//3

            outfits_border = pygame.Rect(0, 0, buttonwidth, screensize[1]//6*2)
            play_border = pygame.Rect(0, 0, buttonwidth, screensize[1]//6*2)
            clubs_border = pygame.Rect(0, 0, buttonwidth, screensize[1]//6*2)

            play_border.top = screensize[1]//6*3
            play_border.centerx = screensize[0]//2

            outfits_border.top = screensize[1]//6*3
            outfits_border.right = play_border.left-25

            clubs_border.top = screensize[1]//6*3
            clubs_border.left = play_border.right+25

            pygame.draw.rect(screen, (52, 52, 52), outfits_border, border_radius=outfits_border.height//10)
            pygame.draw.rect(screen, (52, 52, 52), play_border, border_radius=play_border.height//10)
            pygame.draw.rect(screen, (52, 52, 52), clubs_border, border_radius=clubs_border.height//10)

            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()

# startup

#whiteBoard.main_menu()