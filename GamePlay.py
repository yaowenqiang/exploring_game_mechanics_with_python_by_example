import random
import settings
import pygame
from pygame.locals import *

from Explosion import Explosion
from Player import Player
from Alien import Alien


class GamePlay:
    def __init__(self, screen):
        # self.font = pygame.font.SysFont()
        self.font = pygame.font.SysFont('Arial', 20)
        self.title = self.font.render("This is where the game is", True, (255, 255, 255))
        self.title_position = (10, 10)
        self.main_menu = None
        self.text_color = (255, 255, 255)
        self.button_color = (0, 0, 170)
        self.button_over_color = (255, 50, 50)
        self.button_width = 50
        self.button_height = 20
        self.button_rect = [screen.get_width() - self.button_width,
                            0,
                            self.button_width,
                            self.button_height
                            ]
        self.button_font = pygame.font.SysFont('Arial', 15)
        self.button_text = self.button_font.render('Back', True, self.text_color)
        self.mouse_x, self.mouse_y = (0, 0)
        self.player = Player(screen.get_height() - 100)
        self.aliens = []
        self.alien_rows = 5
        self.alien_cols = 15
        self.explosions = []
        for y in range(self.alien_rows):
            for x in range(self.alien_cols):
                self.aliens.append(Alien(x, y, random.randint(0, 1)))

        self.left_border = 50
        self.right_border = screen.get_width() - self.left_border

        self.dx = 2
        self.dy = 10
        self.direction = self.dx

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_y, self.mouse_y = event.pos
                if self.button_rect[0] <= self.mouse_x <= self.button_rect[0] + self.button_rect[2] and \
                        self.button_rect[1] <= self.mouse_y <= self.button_rect[1] + self.button_rect[3]:
                    return self.main_menu

            if event.type == pygame.MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.pos

        self.player.update()

        found = False
        dead_bullets = []
        if self.player.bullets != [] and self.aliens != []:
            for b in self.player.bullets:
                found = False
                for a in pygame.sprite.spritecollide(b, self.aliens, 0):
                    self.aliens.remove(a)
                    self.explosions.append(Explosion(a.x, a.y))
                    a.kill()
                    found = True

                if found:
                    dead_bullets.append(b)

                # 如果子弹已经飞出屏幕，则可以进行销毁
                if b.y <= 0 and b not in dead_bullets:
                    dead_bullets.append(b)

        for b in dead_bullets:
            self.player.bullets.remove(b)
            b.kill()
        return self

    def draw(self, screen):
        if self.button_rect[0] <= self.mouse_x <= self.button_rect[0] + self.button_rect[2] and \
                self.button_rect[1] <= self.mouse_y <= self.button_rect[1] + self.button_rect[3]:
            pygame.draw.rect(screen, self.button_over_color, self.button_rect)
        else:
            pygame.draw.rect(screen, self.button_color, self.button_rect)

        screen.blit(self.button_text, (self.button_rect[0] + (self.button_width - self.button_text.get_width()) / 2,
                                       self.button_rect[1] + (self.button_height - self.button_text.get_height()) / 2))

        for a in self.aliens:
            a.draw(screen)
        self.player.draw(screen)

        dead_abullets = []
        for l in settings.abullets:
            if l.y > screen.get_height():
               dead_abullets.append(l)
            l.draw(screen)

        for l in dead_abullets:
            settings.abullets.remove(l)
        update_y = False

        if (settings.x_offset + self.alien_cols * 32) > self.right_border:
            self.direction *= -1
            update_y = True
            settings.x_offset = self.right_border - self.alien_cols * 32

        if settings.x_offset < self.left_border:
            self.direction *= -1
            update_y = True
            settings.x_offset = self.left_border

        settings.x_offset += self.direction

        if update_y:
            settings.y_offset += self.dy

        dead_explosions = []
        for e in self.explosions:
            e.draw(screen)
            if e.frame_y < 0:
                dead_explosions.append(e)

        for e in dead_explosions:
            self.explosions.remove(e)
