import json

from view.match_v import MatchView


class MatchController:

    def __init__(self):
        pass

    def match_answer(self):

        answer = MatchView.match_questions()

        self.elo_pair_to_json()

        try:
            if answer == "1":
                self.list_player_ranking()
                self.match_answer()

            elif answer == "2":
                self.list_player_opponent()
                self.match_answer()

            elif answer == "3":
                with open("player_data.json") as f:
                    data = json.load(f)
                    print(data)
                self.response_round_1()

            elif answer == "4":
                self.tri_player_by_point()
                self.response_other_rounds()

            elif answer != "1" or "2" or "3" or "4":
                print("ERREUR : Votre réponse n'est pas valable.")
                self.match_answer()

        except TypeError or ValueError:
            print(f"ERREUR : Votre réponse n'est pas valable.")
            self.match_answer()

    @staticmethod
    def load_data():

        with open("../player_data.json") as f:
            players = json.loads(f.read())

            return players

    def tri_player_by_elo(self):
        """Tri per elo point"""

        data = self.load_data()

        return sorted(data, key=lambda x: x["Elo"])

    def list_player_ranking(self):

        players = self.load_data()
        for player in range(len(players)):
            print("\n---Joueur {} {}---\n"
                  "-a un elo de {} points\n"
                  "-a {} point(s) elo\n"
                  "-est actuellement classé {}er/ème\n".format(
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Elo"),
                   players[player].get("Point"),
                   player + 1))

    def elo_pair(self):

        pairs = []
        player_list = self.tri_player_by_elo()
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

        with open("../paires_round_1.json", "w") as f:
            json.dump(self.elo_pair(), f, indent=2)

    @staticmethod
    def load_data_round():

        with open("../paires_round_1.json") as f:
            players = json.loads(f.read())

            return players

    def list_player_opponent(self):

        players = self.load_data_round()
        for player in range(len(players)):
            print("{} - {} {} ({} points) vs {} - {} {} ({} points)\n".format(
                   player + 1,
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Point"),
                   player + 1,
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Point")))

    @staticmethod
    def load_data_elo_pair():

        with open("../paires_round_1.json") as f:
            players_by_elo = json.loads(f.read())

            return players_by_elo

    def show_player_name(self):

        all_players_name = []
        maxi = len(self.load_data_elo_pair())

        players = self.load_data_elo_pair()
        for x in range(maxi):
            for row in players[x]:
                player_name = row["Nom"]
                all_players_name.append(player_name)
                x += 1

        return all_players_name

    def result_round_1(self):
        """Round 1 results"""

        all_winner = []
        all_loser = []
        all_equality_1 = []
        all_equality_2 = []

        print("Voici la liste des match : ")
        a = 0
        b = 1
        for x in range(len(self.show_player_name()) // 2):
            print(f"Match {x + 1} - "
                  f"{self.show_player_name()[a]} "
                  f"vs "
                  f"{self.show_player_name()[b]}")
            a += 2
            b += 2
            winner = input("Vainqueur = ")
            all_winner.append(winner)
            loser = input("Perdant = ")
            all_loser.append(loser)
            equality_1 = input("Égalité (j1) : ")
            all_equality_1.append(equality_1)
            equality_2 = input("Égalité (j2) : ")
            all_equality_2.append(equality_2)

        return all_winner, all_loser, all_equality_1, all_equality_2
