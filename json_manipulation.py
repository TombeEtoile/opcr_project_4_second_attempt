import json

from controller.menu_c import MenuController


class SetUpJson:

    def load_json(self):

        print("==========LANCEMENT DU PROGRAMME==========\n")

        user_input = input("Entrez 'OK' pour démarrer le programme : ")

        try:
            if user_input == "OK":
                self.player_data()
                self.tournament_data()
                calling_menu = MenuController()
                calling_menu.menu_answer()

            else:
                self.load_json()

        except ValueError:
            self.load_json()

    @staticmethod
    def player_data():
        """creat Json for players"""

        with open("player_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)

            pass

    @staticmethod
    def tournament_data():
        """creat Json for tournaments"""

        with open("tournament_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)

            pass
