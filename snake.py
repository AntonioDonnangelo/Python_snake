import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Snake:
    def __init__(self, position_x, position_y, change_x, change_y, width, heigth, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.heigth = heigth
        self.color = color

    def draw(self):
        """ Draw snake with the instance variables we have. """
        arcade.draw_rectangle_filled(self.position_x, 
                                     self.position_y,
                                     self.width,
                                     self.heigth,
                                     self.color)

    def update(self):
        # Move snake
        self.position_x += self.change_x
        self.position_y += self.change_y


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.APPLE_GREEN)

        # Create snake
        self.snake = Snake(50, 50, 0, 0, 15, 12, arcade.color.BEIGE)

    def on_draw(self):
        """ Called whenever need to draw """
        arcade.start_render()
        self.snake.draw()

        # Draw food
        arcade.draw_circle_filled(300, 300, 5, arcade.color.RED)


    def update(self, delta_time):
        self.snake.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.snake.change_x = -MOVEMENT_SPEED
        if key == arcade.key.RIGHT:
            self.snake.change_x = MOVEMENT_SPEED
        if key == arcade.key.UP:
            self.snake.change_y = MOVEMENT_SPEED
        if key == arcade.key.DOWN:
            self.snake.change_y = -MOVEMENT_SPEED



def main():
    window = MyGame(640, 480, "SNAKE")
    arcade.run()


main()