#установите в терминале..pygame..sys .

import pygame
from pygame.locals import *
import sys
import time
import random


class Game:
    def __init__(self):
        self.w, self.h = 750, 500
        self.reset = True
        self.active = False
        self.timer_started = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = 0
        self.results = 'Time: 0  Accuracy: 0%  WPM: 0'
        self.wpm = 0
        self.end = False

        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()
        self.open_img = pygame.image.load('type-speed.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))

        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Typing Speed Test')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        lines = msg.split('\n')  # Разбиваем текст на несколько строк по символу новой строки
        line_height = fsize + 5  # Расстояние между строками
        for i, line in enumerate(lines):
            text = font.render(line, True, color)
            text_rect = text.get_rect(center=(self.w / 2, y + i * line_height))  # Сдвигаем по вертикали для каждой строки
            screen.blit(text, text_rect)

    def get_sentence(self):
        try:
            with open('sentences.txt', 'r') as f:
                sentences = f.read().split('\n')
                sentences = [s.strip() for s in sentences if s.strip()]
                return random.choice(sentences) if sentences else "Type this default sentence."
        except FileNotFoundError:
            return "Sentence file not found."

    def show_results(self, screen):
        if not self.end:
            self.total_time = time.time() - self.time_start

            correct_chars = sum(1 for i, c in enumerate(self.word)
                                if i < len(self.input_text) and self.input_text[i] == c)
            self.accuracy = (correct_chars / len(self.word)) * 100 if self.word else 0

            self.wpm = len(self.input_text) * 60 / (5 * self.total_time) if self.total_time > 0 else 0
            self.end = True

            self.results = f'Time: {round(self.total_time)} sec   Accuracy: {round(self.accuracy)}%   WPM: {round(self.wpm)}'

            self.time_img = pygame.image.load('icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))

            pygame.draw.rect(screen, (200, 200, 200), (310, 390, 130, 40), 2)
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))
            self.draw_text(screen, self.results, 350, 28, self.RESULT_C)
            pygame.display.update()

    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))
        pygame.display.update()
        time.sleep(1)

        self.reset = False
        self.end = False
        self.active = False
        self.timer_started = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        self.word = self.get_sentence()
        if not self.word:
            self.reset_game()
            return

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.draw_text(self.screen, "Typing Speed Test\nPress ENTER to finish", 80, 80, self.HEAD_C)

        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)
        self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

        pygame.display.update()

    def run(self):
        self.reset_game()
        clock = pygame.time.Clock()
        self.running = True

        while self.running:
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 650 and 250 <= y <= 300:
                        if not self.timer_started:
                            self.active = True
                            self.input_text = ''
                            self.time_start = time.time()
                            self.timer_started = True

                    if 310 <= x <= 440 and 390 <= y <= 430 and self.end:
                        self.reset_game()

                elif event.type == pygame.KEYDOWN and self.active and not self.end:
                    if event.key == pygame.K_RETURN:
                        self.show_results(self.screen)

                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]

                    else:
                        self.input_text += event.unicode

            clock.tick(60)

if __name__ == "__main__":
    Game().run()