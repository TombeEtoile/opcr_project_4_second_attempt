import json

from view.match_v import MatchView
from data.load_data import LoadPlayerData, LoadTournamentData


class MatchController:

    def __init__(self):
        pass

    def match_answer(self):

        answer = MatchView.match_questions()

        try:
            if answer == "1":
                LoadPlayerData.list_player_by_elo()
                self.match_answer()

            elif answer == "2":
                LoadPlayerData.list_player_by_point()
                self.match_answer()

            elif answer == "3":
                self.elo_pair_to_json()
                self.match_answer()

            elif answer == "4":
                pass
                pass

            elif answer != "1" or "2" or "3" or "4":
                print("ERREUR : Votre réponse n'est pas valable.")
                self.match_answer()

        except TypeError or ValueError:
            print("ERREUR : Votre réponse n'est pas valable.")
            self.match_answer()

    def elo_pair(self):

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

    def elo_pair_to_json(self):

        with open("../data/round_1_data.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)


answer = MatchController()
# answer.match_answer()
