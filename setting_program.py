import json

from controller.menu_c import MenuController


class SetUpJson:

    def load_json(self):

        print("\n==========LANCEMENT DU PROGRAMME==========\n")

        user_input = input("Bonjour, bienvenue dans ce programme d'instanciation de tournoi d'échec.\n"
                           "Pour démarrer le programme pour la 1ère fois - entrez '1'\n"
                           "Pour reprendre votre session - entrez '2'\n"
                           "ATTENTION - '1' écrasera vos données sauvegardées\n\n"
                           "Entrez votre réponse : ")

        try:
            if user_input == "1":
                self.player_data()
                self.tournament_data()
                self.round_1_data()
                self.round_2_data()
                self.round_3_data()
                self.round_4_data()

            elif user_input == "2":
                pass

            else:
                print("\nERREUR : valeur inconnue")
                self.load_json()

        except ValueError:
            print("\nERREUR : valeur inconnue")
            self.load_json()

    @staticmethod
    def player_data():
        """creat Json for players"""

        with open("data/player_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)

    @staticmethod
    def tournament_data():
        """creat Json for tournaments"""

        with open("data/tournament_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)

    @staticmethod
    def round_1_data():
        """creat Json for tournaments"""

        with open("data/round_1_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)

    @staticmethod
    def round_2_data():
        """creat Json for tournaments"""

        with open("data/round_2_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)

    @staticmethod
    def round_3_data():
        """creat Json for tournaments"""

        with open("data/round_3_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)

    @staticmethod
    def round_4_data():
        """creat Json for tournaments"""

        with open("data/round_4_data.json", "w+") as f:
            data = []
            json.dump(data, f, indent=2)
