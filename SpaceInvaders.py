from Game import Game
from MainMenu import MainMenu
game = Game("Space Invaders", 800, 800)
main_menu = MainMenu()
game.run(main_menu)