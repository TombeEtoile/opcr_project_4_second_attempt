import json_manipulation
from controller.menu_c import MenuController


def main():

    creat_json = json_manipulation
    creat_json.player_data()
    """Creates an empty Json for players"""
    creat_json.tournament_data()
    """Creates an empty Json for Tournaments"""

    menu = MenuController()
    menu.menu_answer()
    """Calls up the general menu"""


print(main())
