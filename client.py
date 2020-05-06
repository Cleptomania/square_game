import arcade
from network import Network
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Square Game"

MAX_SPEED = 3

ACCELERATION_RATE = 0.3

FRICTION = 0.04

client_number = 0


class SquareGame(arcade.Window):
    """
    Main game class
    """

    def __init__(self, width, height, title):
        """
        Initialize game
        """

        super().__init__(width, height, title)

        self.network = Network()

        self.player = self.network.get_p()
        self.player2 = Player(0, 0, 0, 0, (0, 0, 0))

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen
        """

        arcade.start_render()

        arcade.draw_rectangle_filled(
            self.player.rect.x,
            self.player.rect.y,
            self.player.rect.width,
            self.player.rect.height,
            self.player.color,
        )

        arcade.draw_rectangle_filled(
            self.player2.rect.x,
            self.player2.rect.y,
            self.player2.rect.width,
            self.player2.rect.height,
            self.player2.color,
        )

    def on_update(self, delta_time):
        """
        Movement and Game Logic
        """

        self.player2 = self.network.send(self.player)

        if self.player is not None:
            # Add Friction to Player Movement
            if self.player.change_x > FRICTION:
                self.player.change_x -= FRICTION
            elif self.player.change_x < -FRICTION:
                self.player.change_x += FRICTION
            else:
                self.player.change_x = 0

            if self.player.change_y > FRICTION:
                self.player.change_y -= FRICTION
            elif self.player.change_y < -FRICTION:
                self.player.change_y += FRICTION
            else:
                self.player.change_y = 0

            # Apply Acceleration based on keys pressed
            if self.up_pressed and not self.down_pressed:
                self.player.change_y += ACCELERATION_RATE
            elif self.down_pressed and not self.up_pressed:
                self.player.change_y += -ACCELERATION_RATE

            if self.left_pressed and not self.right_pressed:
                self.player.change_x += -ACCELERATION_RATE
            elif self.right_pressed and not self.left_pressed:
                self.player.change_x += ACCELERATION_RATE

            # Cap player speed
            if self.player.change_x > MAX_SPEED:
                self.player.change_x = MAX_SPEED
            elif self.player.change_x < -MAX_SPEED:
                self.player.change_x = -MAX_SPEED
            if self.player.change_y > MAX_SPEED:
                self.player.change_y = MAX_SPEED
            elif self.player.change_y < -MAX_SPEED:
                self.player.change_y = -MAX_SPEED

            # Update the playuer
            self.player.update()

    def on_key_press(self, symbol, modifiers):
        """Called whenever a key is pressed"""

        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.up_pressed = True
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.down_pressed = True
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.left_pressed = True
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, _symbol, _modifiers):
        """Called whenever a key is released"""

        if _symbol == arcade.key.UP or _symbol == arcade.key.W:
            self.up_pressed = False
        elif _symbol == arcade.key.DOWN or _symbol == arcade.key.S:
            self.down_pressed = False
        elif _symbol == arcade.key.LEFT or _symbol == arcade.key.A:
            self.left_pressed = False
        elif _symbol == arcade.key.RIGHT or _symbol == arcade.key.D:
            self.right_pressed = False


def main():
    """Main Method"""
    window = SquareGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
