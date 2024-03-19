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
                """Closing registrations"""
                # self.return_to_menu()
                pass

            elif response == "6":
                """Return to menu"""
                pass

            elif response != "1" or "2" or "3" or "4" or "5":
                print("ERREUR : Vous devez écrire 1, 2, 3, 4, 5 ou 6")
                self.player_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2, 3, 4, 5 ou 6")
            self.player_answer()

    def add_player(self):

        data = []

        new_player = PlayerInstantiate.get_player_data()
        data.append(new_player)

        with open("player_data.json", "w+") as f:
            json.dump(data, f, indent=2)

        self.player_answer()

        return data

    def check_player_list(self):

        print(self.add_player())
        self.player_answer()

    def add_player_to_json(self):

        data = self.add_player()
        with open("player_data.json", "w+") as f:
            json.dump(data, f, indent=2)

        self.player_answer()

    def edit_player(self):
        pass

    def delete_player(self):
        pass

    # @staticmethod
    # def return_to_menu():

        # menu = MenuController()

        # return menu.menu_view_answer()
