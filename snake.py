# importing libraries
import arcade 

def main():
    #Set a window
    arcade.open_window(700,600,"SNAKE")

    # Set the background color
    arcade.set_background_color(arcade.csscolor.YELLOW_GREEN)

    # Get ready to draw
    arcade.start_render()


    snake = arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
    food = arcade.draw_circle_filled(100, 220, 10, arcade.csscolor.RED)

    # Finish drawing
    arcade.finish_render()

    arcade.run()

main()