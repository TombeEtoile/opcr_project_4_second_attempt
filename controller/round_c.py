import json

from view.round_v import RoundView, PreRoundView
from data.load_data_match import LoadPlayerData


class PreRoundController:

    def __init__(self):
        pass

    def pre_round_answer(self):

        answer = PreRoundView().pre_round_questions()

        tournament = self.load_tournament_name()
        all_tournaments = int(len(self.load_tournament_name())) - int(len(self.load_tournament_name()))

        try:
            if answer == tournament[all_tournaments]:
                print("tournois 1")

            elif answer == tournament[all_tournaments + 1]:
                print("tournois 2")

            else:
                print("ERREUR : Votre réponse n'est pas valable.")
                self.pre_round_answer()

        except ValueError:
            print("ERREUR : Votre réponse n'est pas valable.")
            self.pre_round_answer()

    @staticmethod
    def load_tournament_data():

        with open("../data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments

    def load_tournament_name(self):

        tournaments_name = []

        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            tournaments_name.append(tournament["Nom"])

        return tournaments_name


class RoundController:

    def __init__(self):
        pass

    def round_answer(self):

        answer = RoundView.round_questions()

        try:
            if answer == "1":
                self.round_1_inscription()
                self.round_answer()

            elif answer == "2":
                self.round_2_inscription()
                self.round_answer()

            elif answer == "3":
                self.round_3_inscription()
                self.round_answer()

            elif answer == "4":
                self.round_4_inscription()
                self.round_answer()

            elif answer == "5":
                pass

            elif answer != "1" or "2" or "3" or "4":
                print("ERREUR : Votre réponse n'est pas valable.")
                self.round_answer()

        except TypeError or ValueError:
            print("ERREUR : Votre réponse n'est pas valable.")
            self.round_answer()

    @staticmethod
    def elo_pair():

        pairs = []
        player_list = LoadPlayerData.tri_player_by_elo()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1

        return pairs

    def result_round(self):
        """Round 1 results"""

        winner = []
        loser = []
        equality = []

        print("Voici la liste des match : ")
        a = 0
        b = 1
        for x in range(len(LoadPlayerData.load_player_name()) // 2):
            print(f"---Match {x + 1}---\n"
                  f"{LoadPlayerData.load_player_name()[a]} "
                  f"vs "
                  f"{LoadPlayerData.load_player_name()[b]}")

            user_input = input("Entrez le nom du vainqueur.\n"
                               "Si nul, entrez 'NUL'.\n"
                               "Résultat : ")

            try:
                if user_input == LoadPlayerData.load_player_name()[a]:
                    winner.append(LoadPlayerData.load_player_name()[a])
                    loser.append(LoadPlayerData.load_player_name()[b])

                elif user_input == LoadPlayerData.load_player_name()[b]:
                    winner.append(LoadPlayerData.load_player_name()[b])
                    loser.append(LoadPlayerData.load_player_name()[a])

                elif user_input == "NUL":
                    equality.append(LoadPlayerData.load_player_name()[a])
                    equality.append(LoadPlayerData.load_player_name()[b])

                else:
                    print("Réponse non valide, entrez le prénom du gagant ou entrez 'NUL' si nul")
                    self.result_round()

            except ValueError:
                print("Réponse non valide, entrez le prénom du gagant ou entrez 'NUL' si nul")
                self.result_round()

            a += 2
            b += 2

        return winner, loser, equality

    def list_for_point_distribution(self):
        """Création de listes contenant les victoires, défaites et égalités"""

        vote = self.result_round()

        round_1_result = {"Victoire": vote[0], "Défaite": vote[1], "Égalité": vote[2]}

        return round_1_result

    def point_distribution(self):
        """Distribution des points"""

        result_match = self.list_for_point_distribution()
        all_players = LoadPlayerData.load_player_data()

        print(f"result_match = {result_match}")
        print(f"all_players = {all_players}")

        for player in all_players:
            if player["Prenom"] in result_match["Victoire"]:
                player["Point"] += 1

            elif player["Prenom"] in result_match["Défaite"]:
                player["Point"] += 0

            elif player["Prenom"] in result_match["Égalité"]:
                player["Point"] += 0.5

        with open("data/player_data.json", "w", encoding="utf-8") as fp:
            json.dump(all_players, fp, sort_keys=True, indent=2)

    def round_1_inscription(self):

        self.point_distribution()
        with open("data/round_1_data.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)
        self.round_answer()

    def round_2_inscription(self):

        self.point_distribution()
        with open("data/round_2_data.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)
        self.round_answer()

    def round_3_inscription(self):

        self.point_distribution()
        with open("data/round_3_data.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)
        self.round_answer()

    def round_4_inscription(self):

        self.point_distribution()
        with open("data/round_4_data.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)
        self.round_answer()
