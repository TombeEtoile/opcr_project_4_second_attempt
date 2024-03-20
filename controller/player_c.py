import json

from view.player_v import PlayerView, PlayerInstantiate
# from controller.menu_c import MenuController


class PlayerController:

    def __init__(self):
        pass

    def player_answer(self):

        response = PlayerView.player_questions()

        try:
            if response == "1":
                """add player"""
                self.add_player()

            elif response == "2":
                """check list of player"""
                self.check_player_list()

            elif response == "3":
                """modify player list"""
                self.edit_player()

            elif response == "4":
                """delete player in the list"""
                self.delete_player()

            elif response == "5":
                """Return to menu"""
                self.return_to_menu()

            elif response != "1" or "2" or "3" or "4" or "5":
                print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
                self.player_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
            self.player_answer()

    def add_player(self):

        new_player = PlayerInstantiate.get_player_data()

        with open("../player_data.json", "ab+") as f:
            if f.tell() == 2:
                f.seek(-2, 2)
                f.truncate()
                f.write(b'[\n')
            else:
                f.seek(-2, 2)
                f.truncate()
                f.write(b',\n')
            f.write(json.dumps(new_player, indent=2).encode())
            f.write(b'\n]')

        self.player_answer()

    def check_player_list(self):

        with open("../player_data.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            self.player_answer()

            return player_data

    def edit_player(self):
        pass

    def delete_player(self):
        pass

    @staticmethod
    def return_to_menu():

        pass


test = PlayerController()
test.add_player()
