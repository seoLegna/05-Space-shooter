import arcade 

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
SCREEN_TITLE = "MY GAME"

PLAYER_MOVEMENT_SPEED = 25

class my_game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.alien_list = None
        self.ship_list = None 

        self.ship_sprite = None 
        self.alien_sprite = None

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WARM_BLACK)

    def setup(self):
        self.ship_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()

        self.ship_sprite = arcade.Sprite("images\ship.png")
        self.ship_sprite.center_x = 300
        self.ship_sprite.center_y = 300
        self.ship_list.append(self.ship_sprite)

        self.alien_sprite = arcade.Sprite("images\Alien.png")
        self.alien_sprite.center_x = 500
        self.alien_sprite.center_y = 700
        self.alien_list.append(self.alien_sprite)

    def on_draw(self):
        arcade.start_render()

        self.ship_list.draw()
        self.alien_list.draw()

        x = 250
        y = 600
        radius = 100
        arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE_SMOKE)

        x = 270
        y = 630
        radius = 30
        arcade.draw_circle_filled(x, y, radius, arcade.color.ASH_GREY)

        import random 
        for i in range(20):
            x = random.choice(range(0, 901))
            y = random.choice(range(0, 901))
            radius = 3
            arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship_sprite.center_x = x
        self.ship_sprite.center_y = y

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.ship_sprite.change_y = PLAYER_MOVEMENT_SPEED
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.ship_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.ship_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.ship_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.ship_sprite.change_y = 0
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.ship_sprite.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.ship_sprite.change_x = 0
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.ship_sprite.change_x = 0

    def update(self, delta_time):
        self.ship_sprite.center_x += self.ship_sprite.change_x
        self.ship_sprite.center_y += self.ship_sprite.change_y

def main():
    window = my_game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()