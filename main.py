import setting_program
from controller.menu_c import MenuController


def main():

    creat_json = program_loading.SetUpJson()
    creat_json.load_json()
    """Creates an empty Json for players_data, tournaments_data, all_rounds_data"""

    calling_menu = MenuController()
    calling_menu.menu_answer()
    """Calls up the general menu"""


print(main())
