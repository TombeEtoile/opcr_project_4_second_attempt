import json
import os

from view.menu_v import MenuView
from controller.tournament_c import TournamentController
from controller.player_c import PlayerController
from controller.match_c import MatchController


class MenuController:
    """user-selected routing from the menu_v"""

    def __init__(self):
        pass

    def menu_answer(self):

        try:
            while 1:
                response = MenuView.menu_questions()

                if response == "1":
                    player = PlayerController()
                    player.player_answer()

                elif response == "2":
                    self.call_tournament_c()

                elif response == "3":
                    folder_and_file = CreatingFolderAndFile()
                    folder_and_file.folder_creation()
                    folder_and_file.json_creation()
                    self.call_match_c()

                elif response == "4":
                    quit()

                elif response != "1" or "2" or "3" or "4":
                    print("ERREUR : Vous devez écrire 1, 2, 3 ou 4")
                    self.menu_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2 ou 3")
            self.menu_answer()

    @staticmethod
    def call_player_c():
        """Call player_c"""

        player = PlayerController()

        return player.player_answer()

    @staticmethod
    def call_tournament_c():
        """Call tournament_c"""

        tournament = TournamentController()

        return tournament.tournament_answer()

    @staticmethod
    def call_match_c():
        """Call match_c"""

        match = MatchController()

        return match.match_answer()


class CreatingFolderAndFile:

    def __init__(self):

        pass

    @staticmethod
    def load_player_data():
        """Load player data"""

        with open("data/player_data.json") as f:
            players = json.loads(f.read())

            return players

    @staticmethod
    def load_tournament_data():
        """Load tournament data"""

        with open("data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments

    def load_player_name(self):
        """Load the name of all the players"""

        player_name = []

        players = self.load_player_data()
        for player in players:
            player_name.append(player["Prenom"])

        return player_name

    def load_tournament_name(self):
        """Call the name of all the tournaments"""

        tournaments_name = []

        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            tournaments_name.append(tournament["Nom"])

        return tournaments_name

    def folder_creation(self):
        """Creat one folder for each tournament in tournament_data"""

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
                os.makedirs(f"data/{cleaner_name}", exist_ok=True)
                print(f"- Création du dossier {cleaner_name}")

            elif os.path.exists(f"data/{cleaner_name}"):
                print(f"- Le dossier '{cleaner_name}' existe déjà")

    def json_creation(self):
        """Creat one Json for all round of each tournament in tournament data,
        and place it in the appropriate folder"""

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

                if not os.path.exists(f"data/{cleaner_name}/{cleaner_name}_{round_min}.json"):
                    with open(f"data/{cleaner_name}/{cleaner_name}_{round_min}.json", "w") as f:
                        data = []
                        json.dump(data, f, indent=2)
                        f.flush()

                        print(f"- Création du fichier {cleaner_name}_{round_min}.json")

                elif os.path.exists(f"data/{cleaner_name}/{cleaner_name}_{round_min}.json"):
                    print(f"- Le fichier '{cleaner_name}/{cleaner_name}_{round_min}.json' existe déjà")

                round_min += 1

            for tournament_bis in range(int(round_number)):

                if not os.path.exists(f"data/{cleaner_name}/player_data_{cleaner_name}.json"):
                    with open(f"data/{cleaner_name}/player_data_{cleaner_name}.json", "w") as f:
                        data = self.load_player_data()
                        json.dump(data, f, indent=2)
                        f.flush()

                        print(f"- Création du fichier player_data_{cleaner_name}.json")

                elif os.path.exists(f"data/{cleaner_name}/player_data_{cleaner_name}.json"):
                    print(f"- Le fichier 'player_data_{cleaner_name}.json' existe déjà")
