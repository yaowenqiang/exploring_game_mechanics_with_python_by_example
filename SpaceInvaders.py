from Game import Game
from MainMenu import MainMenu
from SecondMenu import SecondMenu
from ThirdMenu import ThirdMenu
game = Game("Space Invaders", 800, 800)
main_menu = MainMenu()
second_menu = SecondMenu()
second_menu.main_menu = main_menu
main_menu.second_menu = second_menu
third_menu = ThirdMenu()
main_menu.third_menu = third_menu
third_menu.main_menu = main_menu

game.run(main_menu)