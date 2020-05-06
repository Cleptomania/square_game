class Rect:
    """A rectangle utility class
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_bounds(self):
        return (self.x, self.y, self.x + self.width, self.y + self.height)


class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
