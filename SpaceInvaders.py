from Game import Game
from MainMenu import MainMenu
from SecondMenu import SecondMenu
game = Game("Space Invaders", 800, 800)
main_menu = MainMenu()
second_menu = SecondMenu()
main_menu.second_menu = second_menu

game.run(main_menu)