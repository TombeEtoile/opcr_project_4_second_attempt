import json
import os

from view.menu_v import MenuView
from controller.tournament_c import TournamentController
from controller.player_c import PlayerController
from controller.match_c import MatchController


class MenuController:
    """Directs the user to the section of their choice"""

    def __init__(self):
        pass

    def menu_answer(self):

        response = MenuView.menu_questions()

        try:
            if response == "1":
                self.call_player_c()

            elif response == "2":
                self.call_tournament_c()

            elif response == "3":
                folder_and_file = CreatingFolderAndFile()
                folder_and_file.folder_creation()
                folder_and_file.json_creation()
                self.call_match_c()

            elif response == "4":
                pass

            elif response != "1" or "2" or "3" or "4":
                print("ERREUR : Vous devez écrire 1, 2, 3 ou 4")
                self.menu_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2 ou 3")
            self.menu_answer()

    @staticmethod
    def call_player_c():

        player = PlayerController()

        return player.player_answer()

    @staticmethod
    def call_tournament_c():

        tournament = TournamentController()

        return tournament.tournament_answer()

    @staticmethod
    def call_match_c():

        match = MatchController()

        return match.match_answer()


class CreatingFolderAndFile:

    def __init__(self):

        pass

    @staticmethod
    def load_tournament_data():

        with open("data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments

    def load_tournament_name(self):

        tournaments_name = []

        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            tournaments_name.append(tournament["Nom"])

        return tournaments_name

    def folder_creation(self):

        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            name = tournament["Nom"]
            lower_name = name.lower()
            cleaner_name = (lower_name
                            .replace(" ", "_")
                            .replace("'", "_")
                            .replace("-", "_")
                            .replace(".", "")
                            .replace("é", "e")
                            .replace("è", "e")
                            .replace("ê", "e")
                            .replace("ô", "o")
                            .replace("à", "a")
                            .replace("â", "a"))

            if not os.path.exists(f"data/{cleaner_name}"):
                os.mkdir(f"data/{cleaner_name}")
                print(f"- Création du dossier {cleaner_name}")

            elif os.path.exists(f"data/{cleaner_name}"):
                print(f"- Le dossier '{cleaner_name}' existe déjà")

    def json_creation(self):

        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            name = tournament["Nom"]
            lower_name = name.lower()
            cleaner_name = (lower_name
                            .replace(" ", "_")
                            .replace("'", "_")
                            .replace("-", "_")
                            .replace(".", "")
                            .replace("é", "e")
                            .replace("è", "e")
                            .replace("ê", "e")
                            .replace("ô", "o")
                            .replace("à", "a")
                            .replace("â", "a"))

            round_number = tournament["Nombre de rounds"]
            round_min = int(round_number) // int(round_number)

            for tournament_bis in range(int(round_number)):

                if not os.path.exists(f"data/{cleaner_name}/{cleaner_name}_{round_min}"):
                    with open(f"data/{cleaner_name}/{cleaner_name}_{round_min}", "w") as f:
                        data = []
                        json.dump(data, f, indent=2)

                        print(f"- Création du fichier {cleaner_name}_{round_min}")

                elif os.path.exists(f"data/{cleaner_name}/{cleaner_name}_{round_min}"):
                    print(f"- Le fichier '{cleaner_name}/{cleaner_name}_{round_min}' existe déjà")

                round_min += 1
