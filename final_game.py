import arcade 
import random
import time

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
SCREEN_TITLE = "MY GAME"

PLAYER_MOVEMENT_SPEED = 15
MARGIN = 55

class my_game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.alien_list = None
        self.ship_list = None 
        self.bullet_list = None

        self.ship_sprite = None 
        self.alien_sprite = None
        self.alien2_sprite = None
        self.alien3_sprite = None
        self.bullet_list = None

        self.score = 0
        self.score_text = None


        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.WARM_BLACK)

    def setup(self):
        self.ship_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0

        self.ship_sprite = arcade.Sprite("images\ship.png",0.5)
        self.ship_sprite.center_x = 300
        self.ship_sprite.center_y = 300
        self.ship_list.append(self.ship_sprite)

        self.alien_sprite = arcade.Sprite("images\Alien.png",0.2)
        self.alien_sprite.center_x = 500
        self.alien_sprite.center_y = 700
        self.alien_list.append(self.alien_sprite)
        self.alien_sprite_health = 10

        self.alien2_sprite = arcade.Sprite("images\Alien2.png",0.2)
        self.alien2_sprite.center_x = 100
        self.alien2_sprite.center_y = 700
        self.alien_list.append(self.alien2_sprite)
        self.alien2_sprite_health = 15

        self.alien3_sprite = arcade.Sprite("images\Alien3.png",0.2)
        self.alien3_sprite.center_x = 800
        self.alien3_sprite.center_y = 700
        self.alien_list.append(self.alien3_sprite)
        self.alien3_sprite_health = 20
        self.alien_velocity_y = -13
        self.alien_velocity_x = 13

        self.bullet_sprite = arcade.Sprite("images\Bullet.png",0.1)
        self.bullet_sprite.center_x = self.ship_sprite.center_x 
        self.bullet_sprite.center_y = self.ship_sprite.center_y
        self.bullet_list.append(self.bullet_sprite)
        self.bullet_velocity_y = 27

    def on_draw(self):
        arcade.start_render()

        self.ship_list.draw()
        self.alien_list.draw()
        self.bullet_list.draw()

        x = 250
        y = 600
        radius = 100
        arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE_SMOKE)

        x = 270
        y = 630
        radius = 30
        arcade.draw_circle_filled(x, y, radius, arcade.color.ASH_GREY)

        for i in range(20):
            x = random.choice(range(0, 901))
            y = random.choice(range(0, 901))
            radius = 3
            arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)

        output = f"Score: {self.score}"
        arcade.draw_text(output, 35, 850, arcade.color.RED_DEVIL, 11)     #  draw_text(output, 13, 23, arcade.color.RED_DEVIL, 15)

        if self.score == 19:
            arcade.draw_text("YOU WIN", 450, 450, arcade.color.WHITE, 12)

        if self.score == -1:
            arcade.draw_text("YOU LOOSE, YOUR SHIP HIT AN ALIEN", 450, 450, arcade.color.BLACK, 12)

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

    def on_mouse_press(self, x, y, button, modifiers):

        if button == arcade.MOUSE_BUTTON_LEFT:
            self.bullet_sprite = arcade.Sprite("images\Bullet.png",0.1) 
            self.bullet_sprite.center_y = y
            self.bullet_sprite.center_x = x
            self.bullet_list.append(self.bullet_sprite)


    def update(self, delta_time):
        self.ship_sprite.center_x += self.ship_sprite.change_x
        self.ship_sprite.center_y += self.ship_sprite.change_y
        bad_hit_list = arcade.check_for_collision_with_list(self.ship_sprite, self.alien_list)
        if len(bad_hit_list) > 0:
            self.ship_sprite.kill()
            self.score = -1


        for self.alien_sprite in self.alien_list: 
            self.alien_sprite.center_x += self.alien_velocity_x
            self.alien_sprite.center_y += self.alien_velocity_y
            if self.alien_sprite.center_y <= MARGIN:
                self.alien_velocity_y = -self.alien_velocity_y
            if self.alien_sprite.center_x <= MARGIN:
                self.alien_velocity_x = -self.alien_velocity_x
            if self.alien_sprite.center_x <= (SCREEN_WIDTH - MARGIN):
                self.alien_velocity_x = -self.alien_velocity_x
            if self.alien_sprite.center_y <= (SCREEN_HEIGHT - MARGIN):
                self.alien_velocity_y = -self.alien_velocity_y
        for self.alien2_sprite in self.alien_list:
            self.alien2_sprite.center_x += self.alien_velocity_x
            self.alien2_sprite.center_y += self.alien_velocity_y
            if self.alien2_sprite.center_y <= MARGIN:
                self.alien_velocity_y = -self.alien_velocity_y
            if self.alien2_sprite.center_x <= MARGIN:
                self.alien_velocity_x = -self.alien_velocity_x
            if self.alien2_sprite.center_x <= (SCREEN_WIDTH - MARGIN):
                self.alien_velocity_x = -self.alien_velocity_x
            if self.alien2_sprite.center_y <= (SCREEN_HEIGHT - MARGIN):
                self.alien_velocity_y = -self.alien_velocity_y
        for self.alien3_sprite in self.alien_list:
            self.alien3_sprite.center_x += self.alien_velocity_x
            self.alien3_sprite.center_y += self.alien_velocity_y
            if self.alien3_sprite.center_y <= MARGIN:
                self.alien_velocity_y = -self.alien_velocity_y
            if self.alien3_sprite.center_x <= MARGIN:
                self.alien_velocity_x = -self.alien_velocity_x
            if self.alien3_sprite.center_x <= (SCREEN_WIDTH - MARGIN):
                self.alien_velocity_x = -self.alien_velocity_x
            if self.alien3_sprite.center_y <= (SCREEN_HEIGHT - MARGIN):
                self.alien_velocity_y = -self.alien_velocity_y


        self.bullet_list.update()
        for self.bullet_sprite in self.bullet_list:
            
            self.bullet_sprite.center_y += self.bullet_velocity_y 

            for self.alien_sprite in self.alien_list:
                no_alien = arcade.check_for_collision(self.bullet_sprite, self.alien_sprite)
                
                if no_alien == True:
                    self.bullet_sprite.kill()
                if no_alien == True:
                    if self.alien_sprite_health != 0:
                        self.alien_sprite_health -= 1
                        self.score += 1
                    if self.alien_sprite_health == 0:
                        self.alien_sprite.kill()
                        self.score += 3

def main():
    window = my_game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()