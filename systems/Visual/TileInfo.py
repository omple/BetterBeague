import pygame.draw


class TileInfo:
    x_pos = None
    y_pos = None
    width = None
    color = None
    letter_pow = None
    word_pow = None

    def __init__(self, x_pos, y_pos, width, letter_pow, word_pow):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.letter_pow = letter_pow
        self.word_pow = word_pow

        if letter_pow == 2:
            self.color = "cadetblue2"
        elif letter_pow == 3:
            self.color = "gold1"
        elif word_pow == 2:
            self.color = "green2"
        elif word_pow == 3:
            self.color = "tomato2"
        elif (self.x_pos + self.y_pos) % 2 == 0:
            self.color = "bisque"
        else:
            self.color = "bisque2"

    def create_rectangle(self, screen, x_offset, y_offset):
        pygame.draw.rect(screen, self.color,
                         pygame.Rect(self.x_pos * self.width + x_offset, self.y_pos * self.width + y_offset, self.width, self.width), 0)
