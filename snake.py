from random import randint
import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Snake:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color

    def draw_snake(self):
        """ Draw snake with the instance variables we have. """
        arcade.draw_rectangle_filled(self.position_x, 
                                     self.position_y,
                                     self.width,
                                     self.height,
                                     self.color)

    def update(self):
        # Move the snake
        self.position_x += self.change_x
        self.position_y += self.change_y


class Food:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw_food(self):
        """ Draw food with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the snake
        self.position_x += self.change_x
        self.position_y += self.change_y


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.APPLE_GREEN)

        # Create snake and food
        self.snake = Snake(randint(300, 300),
                           randint(20, 200),
                           0,
                           0,
                           20,
                           20,
                           arcade.color.BEIGE)
        self.food = Food(randint(300, 300),
                         randint(20, 200),
                         0,
                         0,
                         10,
                         arcade.color.RED)
        self.score = 0
    def on_draw(self):
        """ Called whenever need to draw """
        arcade.start_render()

        # Draw snake
        self.snake.draw_snake()

        # Draw food
        self.food.draw_food()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18,
        )
    def update(self, delta_time):
        if (
                self.snake.position_x - self.snake.width / 2 < self.food.position_x < self.snake.position_x + self.snake.width / 2
                and self.snake.position_y - self.snake.height / 2 < self.food.position_y < self.snake.position_y + self.snake.height / 2
        ):
            # If snake collides with food, update food position
            self.food.position_x = randint(0, SCREEN_WIDTH)
            self.food.position_y = randint(0, SCREEN_HEIGHT)
            self.score += 1

        self.snake.update()
        self.food.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        if key == arcade.key.LEFT:
            self.snake.change_x = -MOVEMENT_SPEED
            self.snake.change_y = 0
        if key == arcade.key.RIGHT:
            self.snake.change_x = MOVEMENT_SPEED
            self.snake.change_y = 0
        if key == arcade.key.UP:
            self.snake.change_y = MOVEMENT_SPEED
            self.snake.change_x = 0
        if key == arcade.key.DOWN:
            self.snake.change_y = -MOVEMENT_SPEED
            self.snake.change_x = 0


def main():
    MyGame(640, 480, "SNAKE")
    arcade.run()


main()
