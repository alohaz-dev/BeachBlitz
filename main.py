# imports

import pygame

# vars

# colours

greenidle = (47, 151, 95) 
greenhover = (73, 177, 121) 

green2idle = (102, 185, 63)
green2hover = (132, 180, 111)

blueidle = (95, 204, 161)
bluehover = (135, 201, 176)

redidle = (211, 101, 75)
redhover = (209, 133, 115)

smoothwhite = (229, 229, 229)
toothpaste = (206, 206, 206)
darkgrey = (26, 26, 26)
darkgrey1 = (52, 52, 52)
darkgrey2 = (78, 78, 78)
darkgrey3 = (104, 104, 104)
darkgrey4 = (130, 130, 130)
errorred = (235, 64, 52)
orchidpurple = (176, 105, 238)
devyellow = (240, 213, 65)
ainspink = (224, 56, 87)

# code

class serverSide():
    def load_window():
        level_ui = pygame.image.load(r'assets\gfx\logo_ui.png')
        pygame.display.set_caption('Beach Blitz')
        pygame.display.set_icon(level_ui)
        screen = pygame.display.set_mode((750, 500), pygame.RESIZABLE)
        mainMenu.main_menu(screen)

class playerPortal():
    def main_portal(screen):
        while True:
            screen.fill(darkgrey)
            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()

class mainMenu():
    def main_menu(screen):
        while True:
            screen.fill(darkgrey)
            pygame.font.init()
            screensize = screen.get_size()
            title_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', screensize[1]//6)
            title_text = title_font.render('beach blitz', True, smoothwhite)
            title_rect = title_text.get_rect()
            title_rect.centerx = screensize[0]//2
            title_rect.top = screensize[1]//6

            subtitle_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', screensize[1]//18)
            subtitle = 'developer mode'
            subtitle_color = devyellow
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

            pygame.draw.rect(screen, darkgrey2, outfits_border, border_radius=outfits_border.height//10)
            pygame.draw.rect(screen, darkgrey2, play_border, border_radius=play_border.height//10)
            pygame.draw.rect(screen, darkgrey2, clubs_border, border_radius=clubs_border.height//10)

            outfits_button = pygame.Rect(0, 0, outfits_border.w-20, outfits_border.h-20)
            play_button = pygame.Rect(0, 0, play_border.w-20, play_border.h-20)
            clubs_button = pygame.Rect(0, 0, clubs_border.w-20, clubs_border.h-20)

            outfits_button.center = outfits_border.center
            play_button.center = play_border.center
            clubs_button.center = clubs_border.center

            mouse = pygame.mouse.get_pos()

            if outfits_button.left <= mouse[0] <= outfits_button.right and outfits_button.top <= mouse[1] <= outfits_button.bottom:
                pygame.draw.rect(screen, bluehover, outfits_button, border_radius=outfits_button.height//10)
            else:
                pygame.draw.rect(screen, blueidle, outfits_button, border_radius=outfits_button.height//10)

            if play_button.left <= mouse[0] <= play_button.right and play_button.top <= mouse[1] <= play_button.bottom:
                pygame.draw.rect(screen, green2hover, play_button, border_radius=play_button.height//10)
            else:
                pygame.draw.rect(screen, green2idle, play_button, border_radius=play_button.height//10)

            if clubs_button.left <= mouse[0] <= clubs_button.right and clubs_button.top <= mouse[1] <= clubs_button.bottom:
                pygame.draw.rect(screen, redhover, clubs_button, border_radius=clubs_button.height//10)
            else:
                pygame.draw.rect(screen, redidle, clubs_button, border_radius=clubs_button.height//10)

            button_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', play_button.height//3)

            outfits_text = button_font.render('outfits', True, smoothwhite)
            play_text = button_font.render('play', True, smoothwhite)
            clubs_text = button_font.render('clubs', True, smoothwhite)

            outfits_text_rect = outfits_text.get_rect()
            play_text_rect = play_text.get_rect()
            clubs_text_rect = clubs_text.get_rect()

            outfits_text_rect.center = outfits_button.center
            play_text_rect.center = play_button.center
            clubs_text_rect.center = clubs_button.center

            screen.blit(outfits_text, outfits_text_rect)
            screen.blit(play_text, play_text_rect)
            screen.blit(clubs_text, clubs_text_rect)

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

            circle_buttons_size = (waffle_ui_rect.right-friends_ui_rect.left-20)//2

            banners_ui = pygame.image.load(r'assets\gfx\banners_ui.png')
            banners_ui_scaled = pygame.transform.scale(banners_ui, (circle_buttons_size, circle_buttons_size))
            banners_ui_rect = banners_ui_scaled.get_rect()
            banners_ui_rect.top = waffle_ui_rect.bottom+screensize[1]//18-18
            banners_ui_rect.right = waffle_ui_rect.right
            screen.blit(banners_ui_scaled, banners_ui_rect)

            quests_ui = pygame.image.load(r'assets\gfx\quests_ui.png')
            quests_ui_scaled = pygame.transform.scale(quests_ui, (circle_buttons_size, circle_buttons_size))
            quests_ui_rect = quests_ui_scaled.get_rect()
            quests_ui_rect.top = friends_ui_rect.bottom+screensize[1]//18-18
            quests_ui_rect.left = friends_ui_rect.left
            screen.blit(quests_ui_scaled, quests_ui_rect)

            pass_border = None # pygame.Rect()

            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    #quit()
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.left <= mouse[0] <= play_button.right and play_button.top <= mouse[1] <= play_button.bottom:
                        playMenu.tug_of_war(screen)

class whiteBoard():
    def main_menu(screen):
        screen = pygame.display.set_mode((750, 500), pygame.RESIZABLE)
        while True:
            screen.fill(darkgrey)
            pygame.font.init()
            screensize = screen.get_size()
            title_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', screensize[1]//6)
            title_text = title_font.render('beach blitz', True, smoothwhite)
            title_rect = title_text.get_rect()
            title_rect.centerx = screensize[0]//2
            title_rect.top = screensize[1]//6

            subtitle_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', screensize[1]//18)
            subtitle = 'developer mode'
            subtitle_color = devyellow
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

            pygame.draw.rect(screen, darkgrey2, outfits_border, border_radius=outfits_border.height//10)
            pygame.draw.rect(screen, darkgrey2, play_border, border_radius=play_border.height//10)
            pygame.draw.rect(screen, darkgrey2, clubs_border, border_radius=clubs_border.height//10)

            outfits_button = pygame.Rect(0, 0, outfits_border.w-20, outfits_border.h-20)
            play_button = pygame.Rect(0, 0, play_border.w-20, play_border.h-20)
            clubs_button = pygame.Rect(0, 0, clubs_border.w-20, clubs_border.h-20)

            outfits_button.center = outfits_border.center
            play_button.center = play_border.center
            clubs_button.center = clubs_border.center

            mouse = pygame.mouse.get_pos()

            if outfits_button.left <= mouse[0] <= outfits_button.right and outfits_button.top <= mouse[1] <= outfits_button.bottom:
                pygame.draw.rect(screen, bluehover, outfits_button, border_radius=outfits_button.height//10)
            else:
                pygame.draw.rect(screen, blueidle, outfits_button, border_radius=outfits_button.height//10)

            if play_button.left <= mouse[0] <= play_button.right and play_button.top <= mouse[1] <= play_button.bottom:
                pygame.draw.rect(screen, green2hover, play_button, border_radius=play_button.height//10)
            else:
                pygame.draw.rect(screen, green2idle, play_button, border_radius=play_button.height//10)

            if clubs_button.left <= mouse[0] <= clubs_button.right and clubs_button.top <= mouse[1] <= clubs_button.bottom:
                pygame.draw.rect(screen, redhover, clubs_button, border_radius=clubs_button.height//10)
            else:
                pygame.draw.rect(screen, redidle, clubs_button, border_radius=clubs_button.height//10)

            button_font = pygame.font.Font(r'assets\gfx\mainfont.ttf', play_button.height//3)

            outfits_text = button_font.render('outfits', True, smoothwhite)
            play_text = button_font.render('play', True, smoothwhite)
            clubs_text = button_font.render('clubs', True, smoothwhite)

            outfits_text_rect = outfits_text.get_rect()
            play_text_rect = play_text.get_rect()
            clubs_text_rect = clubs_text.get_rect()

            outfits_text_rect.center = outfits_button.center
            play_text_rect.center = play_button.center
            clubs_text_rect.center = clubs_button.center

            screen.blit(outfits_text, outfits_text_rect)
            screen.blit(play_text, play_text_rect)
            screen.blit(clubs_text, clubs_text_rect)

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

            circle_buttons_size = (waffle_ui_rect.right-friends_ui_rect.left-20)//2

            banners_ui = pygame.image.load(r'assets\gfx\banners_ui.png')
            banners_ui_scaled = pygame.transform.scale(banners_ui, (circle_buttons_size, circle_buttons_size))
            banners_ui_rect = banners_ui_scaled.get_rect()
            banners_ui_rect.top = waffle_ui_rect.bottom+screensize[1]//18-18
            banners_ui_rect.right = waffle_ui_rect.right
            screen.blit(banners_ui_scaled, banners_ui_rect)

            quests_ui = pygame.image.load(r'assets\gfx\quests_ui.png')
            quests_ui_scaled = pygame.transform.scale(quests_ui, (circle_buttons_size, circle_buttons_size))
            quests_ui_rect = quests_ui_scaled.get_rect()
            quests_ui_rect.top = friends_ui_rect.bottom+screensize[1]//18-18
            quests_ui_rect.left = friends_ui_rect.left
            screen.blit(quests_ui_scaled, quests_ui_rect)

            pass_border = None # pygame.Rect()

            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.left <= mouse[0] <= play_button.right and play_button.top <= mouse[1] <= play_button.bottom:
                        playMenu.tug_of_war(screen)

class playMenu():
    def tug_of_war(screen):
        while True:
            screen.fill(darkgrey)
            screensize = screen.get_size()
            main_rect = pygame.Rect(100, 100, screensize[0]-200, screensize[1]-200)
            pygame.draw.rect(screen, darkgrey1, main_rect, border_radius=main_rect.h//10)
            arrow_left_ui = pygame.image.load(r'assets\gfx\arrow_left_ui.png')
            arrow_left_ui_rect = arrow_left_ui.get_rect()
            arrow_left_ui_rect.centery = main_rect.centery
            arrow_left_ui_rect.left = 0
            screen.blit(arrow_left_ui, arrow_left_ui_rect)
            arrow_right_ui = pygame.image.load(r'assets\gfx\arrow_right_ui.png')
            arrow_right_ui_rect = arrow_right_ui.get_rect()
            arrow_right_ui_rect.centery = main_rect.centery
            arrow_right_ui_rect.right = screensize[0]
            screen.blit(arrow_right_ui, arrow_right_ui_rect)
            home_ui = pygame.image.load(r'assets\gfx\home_ui.png')
            screen.blit(home_ui, (0, 0))
            pygame.display.update()
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 10 <= mouse[0] <= 90 and 10 <= mouse[1] <= 90:
                        mainMenu.main_menu(screen)

    def coming_soon_ph(screen, session_id): # the placeholder for a new games
        pass

# startup

serverSide.load_window()