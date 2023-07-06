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

            level_ui = pygame.image.load(r'assets\gfx\level_ui.png')
            level_ui_scaled = pygame.transform.scale(level_ui, (screensize[1]//18*3, screensize[1]//18))
            level_ui_rect = level_ui_scaled.get_rect()
            level_ui_rect.top = screensize[1]//18
            level_ui_rect.left = screensize[1]//18
            screen.blit(level_ui_scaled, level_ui_rect)

            gem_ui = pygame.image.load(r'assets\gfx\gem_ui.png')
            gem_ui_scaled = pygame.transform.scale(gem_ui, (screensize[1]//18*3, screensize[1]//18))
            gem_ui_rect = gem_ui_scaled.get_rect()
            gem_ui_rect.top = screensize[1]//18
            gem_ui_rect.right = screensize[0]-screensize[1]//18
            screen.blit(gem_ui_scaled, gem_ui_rect)

            coin_ui = pygame.image.load(r'assets\gfx\coin_ui.png')
            coin_ui_scaled = pygame.transform.scale(coin_ui, (screensize[1]//18*3, screensize[1]//18))
            coin_ui_rect = coin_ui_scaled.get_rect()
            coin_ui_rect.top = screensize[1]//18
            coin_ui_rect.right = gem_ui_rect.left-screensize[1]//18
            screen.blit(coin_ui_scaled, coin_ui_rect)

            profile_ui = pygame.image.load(r'assets\gfx\profile_ui.png')
            profile_ui_scaled = pygame.transform.scale(profile_ui, (screensize[1]//18, screensize[1]//18))
            profile_ui_rect = profile_ui_scaled.get_rect()
            profile_ui_rect.top = screensize[1]//18
            profile_ui_rect.left = level_ui_rect.right+screensize[1]//18
            screen.blit(profile_ui_scaled, profile_ui_rect)

            buttonside = (gem_ui_rect.right-title_rect.right-screensize[1]//18*2-10)//3

            waffle_ui = pygame.image.load(r'assets\gfx\waffle_ui.png')
            waffle_ui_scaled = pygame.transform.scale(waffle_ui, (buttonside, buttonside))
            waffle_ui_rect = waffle_ui_scaled.get_rect()
            waffle_ui_rect.top = screensize[1]//18*3
            waffle_ui_rect.right = gem_ui_rect.right
            screen.blit(waffle_ui_scaled, waffle_ui_rect)

            news_ui = pygame.image.load(r'assets\gfx\news_ui.png')
            news_ui_scaled = pygame.transform.scale(news_ui, (buttonside, buttonside))
            news_ui_rect = news_ui_scaled.get_rect()
            news_ui_rect.top = screensize[1]//18*3
            news_ui_rect.right = waffle_ui_rect.left-10
            screen.blit(news_ui_scaled, news_ui_rect)

            friends_ui = pygame.image.load(r'assets\gfx\friends_ui.png')
            friends_ui_scaled = pygame.transform.scale(friends_ui, (buttonside, buttonside))
            friends_ui_rect = friends_ui_scaled.get_rect()
            friends_ui_rect.top = screensize[1]//18*3
            friends_ui_rect.right = news_ui_rect.left-10
            screen.blit(friends_ui_scaled, friends_ui_rect)

            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()

# startup

whiteBoard.main_menu()