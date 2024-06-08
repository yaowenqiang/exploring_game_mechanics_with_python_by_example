from Game import Game
from MainMenu import MainMenu
from GamePlay import GamePlay
game = Game("Space Invaders", 800, 800)
main_menu = MainMenu()
game_play = GamePlay(game.screen)
main_menu.gameplay_scene = game_play
game.run(main_menu)