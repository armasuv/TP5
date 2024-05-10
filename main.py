
import game_state, arcade, random, time

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(800, 800, "TP5")

        self.game_state = game_state.GameState.GAME_NOT_STARTED

        self.reset_round()

        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(arcade.Sprite("assets/faceBeard.png", scale=0.3, center_x= 200, center_y=400, ))
        self.sprite_list.append(arcade.Sprite("assets/compy.png", scale=2, center_x= 600, center_y=400, ))

    def reset_round(self):
        self.pointage_usager = 0
        self.pointage_ordinateur = 0

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK)

        if self.game_state == game_state.GameState.GAME_NOT_STARTED:
            arcade.draw_text("ROCHE, PAPIER, CISEAUX!", start_x = 140, start_y = 750, font_size=30, color=arcade.color.RED_BROWN)
            arcade.draw_text("Appuye sur espace pour commencer. ;)", start_x=80, start_y=400, font_size=30, color= arcade.color.BABY_POWDER)

        if self.game_state == game_state.GameState.ROUND_ACTIVE:
            self.not_moving_images()
            arcade.draw_text("Appuye sur une image pour attaquer. ;)", start_x=80, start_y=700, font_size=30,color=arcade.color.BABY_POWDER)
        if self.game_state == game_state.GameState.ROUND_DONE:
            pass

        if self.game_state == game_state.GameState.GAME_OVER:
            pass

    def not_moving_images(self):

        arcade.draw_text(text = "Le pointage du joueur:%d"%self.pointage_usager, start_x=50, start_y=100, font_size=15,color=arcade.color.RED_BROWN)
        arcade.draw_text(text = "Le pointage de l'ordi:%d"%self.pointage_ordinateur, start_x=550, start_y=100, font_size=15,color=arcade.color.BABY_POWDER)

        arcade.draw_rectangle_outline(center_x=90, center_y=200, width = 100, height= 100, color=arcade.color.DIAMOND)
        arcade.draw_rectangle_outline(center_x=200, center_y=200, width = 100, height= 100, color=arcade.color.DIAMOND)
        arcade.draw_rectangle_outline(center_x=310, center_y=200, width = 100, height= 100, color=arcade.color.DIAMOND)
        arcade.draw_rectangle_outline(center_x=600, center_y=200, width = 100, height= 100, color=arcade.color.DIAMOND)

        self.sprite_list.draw()
    def on_key_press(self, symbol, modifiers):
        if symbol == 32 and self.game_state == game_state.GameState.GAME_NOT_STARTED:
            self.game_state = game_state.GameState.ROUND_ACTIVE
def main():
    mygame = MyGame()
    mygame.on_draw

    arcade.run()
main()