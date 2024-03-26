import json


class LoadPlayerData:

    @staticmethod
    def load_player_data():

        with open("data/player_data.json") as f:
            players = json.loads(f.read())

            return players

    @staticmethod
    def load_player_name():

        player_name = []

        players = LoadPlayerData.load_player_data()
        for player in players:
            player_name.append(player["Prenom"])

        return player_name

    @staticmethod
    def tri_player_by_elo():
        """Tri per elo point"""

        data = LoadPlayerData.load_player_data()

        return sorted(data, reverse=True, key=lambda x: x["Elo"])

    @staticmethod
    def tri_player_by_point():
        """Tri per elo point"""

        data = LoadPlayerData.load_player_data()

        return sorted(data, reverse=True, key=lambda x: x["Point"])

    @staticmethod
    def list_player_by_elo():

        print("\n-----Liste des joueurs triés par elo-----\n")

        players = LoadPlayerData.tri_player_by_elo()
        x = len(players)
        for player in range(x):
            print("\n---{}er/ème : {} {}---\n"
                  "   -a un elo de {}\n"
                  "   -a {} point(s)\n".format(
                   player + 1,
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Elo"),
                   players[player].get("Point")))

    @staticmethod
    def list_player_by_point():

        print("\n-----Liste des joueurs triés par point de compétition-----\n")

        players = LoadPlayerData.tri_player_by_point()
        x = len(players)
        for player in range(x):
            print("\n---{}er/ème : {} {}---\n"
                  "   -a un elo de {}\n"
                  "   -a {} point(s)\n".format(
                   player + 1,
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Elo"),
                   players[player].get("Point")))


class LoadTournamentData:

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


class LoadRoundData:

    @staticmethod
    def load_round_1_data():

        with open("data/round_1_data.json") as f:
            players = json.loads(f.read())

            return players

    @staticmethod
    def see_round_1():

        print("\n-----Round n°1-----\n")

        players = LoadRoundData.load_round_1_data()
        x = len(players) / 2
        for player in players:
            for number in range(int(x)):
                print("     ---{} {}---\n"
                      "elo = {} / point(s) = {}\n"
                      "          vs\n"
                      "     ---{} {}---\n"
                      "elo = {} / point(s) = {}\n".format(
                       player[number].get("Prenom"),
                       player[number].get("Nom"),
                       player[number].get("Elo"),
                       player[number].get("Point"),

                       player[number + 1].get("Prenom"),
                       player[number + 1].get("Nom"),
                       player[number + 1].get("Elo"),
                       player[number + 1].get("Point"),
                       number + 2))

    @staticmethod
    def test_modification_json():

        players = LoadPlayerData.load_player_data()

        for player in players:
            player["Point"] = +1

        with open("test.json", "w", encoding="utf-8") as fp:
            json.dump(players, fp, sort_keys=True, indent=4)

    @staticmethod
    def load_test():

        with open("test.json") as f:
            players = json.loads(f.read())

            return players


# player = LoadPlayerData
# print(player.load_player_data())

# round = LoadRoundData()
# round.test_modification_json()
# print(round.load_test())
