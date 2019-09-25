import arcade 

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "A smile")

arcade.set_background_color(arcade.color.AERO_BLUE)

arcade.start_render()

x = 300
y = 400
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.RED_DEVIL)

x = 230
y = 450
radius = 30
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 370
y = 450
radius = 30
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 300
y = 370
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle)

arcade.finish_render()

arcade.run()
