from systems.Visual import Constants
from systems.Visual.TileInfo import TileInfo


class BoardInfo:
    grid = []
    x_offset = None
    y_offset = None
    screen = None

    def __init__(self, screen, x_offset, y_offset):
        self.screen = screen
        self.x_offset = x_offset
        self.y_offset = y_offset

        for f in range(Constants.BOARD_WIDTH):
            newRow = []
            for i in range(Constants.BOARD_LENGTH):
                letter_pow = 1
                word_pow = 1

                if Constants.LETTER2LIST.__contains__([i, f]):
                    letter_pow = 2
                elif Constants.LETTER3LIST.__contains__([i,f]):
                    letter_pow = 3

                if Constants.WORD2LIST.__contains__([i, f]):
                    word_pow = 2
                elif Constants.WORD3LIST.__contains__([i, f]):
                    word_pow = 3

                tile = TileInfo(i, f, Constants.BOX_WIDTH, letter_pow, word_pow)
                newRow.append(tile)
            self.grid.append(newRow)

    def draw(self):
        for f in range(19):
            for i in range(27):
                self.grid[f][i].create_rectangle(self.screen, self.x_offset, self.y_offset)
