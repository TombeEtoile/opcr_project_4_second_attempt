import json


class LoadPlayerData:

    @staticmethod
    def load_player_data():

        with open("../data/player_data.json") as f:
            players = json.loads(f.read())

            return players

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
            print("\n---Joueur {} {}---\n"
                  "-a un elo de {}\n"
                  "-a {} point(s)\n"
                  "-est actuellement classé {}er/ème\n".format(
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Elo"),
                   players[player].get("Point"),
                   player + 1))

    @staticmethod
    def list_player_by_point():

        print("\n-----Liste des joueurs triés par point de compétition-----\n")

        players = LoadPlayerData.tri_player_by_point()
        x = len(players)
        for player in range(x):
            print("\n---Joueur {} {}---\n"
                  "-a un elo de {}\n"
                  "-a {} point(s)\n"
                  "-est actuellement classé {}er/ème\n".format(
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Elo"),
                   players[player].get("Point"),
                   player + 1))


class LoadTournamentData:

    @staticmethod
    def load_tournament_data():

        with open("../data/tournament_data.json") as f:
            players = json.loads(f.read())

            return players


class LoadRoundData:

    @staticmethod
    def load_round_1_data():

        with open("../data/round_1_data.json") as f:
            players = json.loads(f.read())

            return players

    @staticmethod
    def see_round_1():

        print("\n-----Round n°1-----\n")

        players = LoadRoundData.load_round_1_data()
        x = len(players) / 2
        for player in players:
            print(player)
            for number in range(x):
                print("\n---Joueur {} {}---\n"
                      "-a un elo de {}\n"
                      "-a {} point(s)\n"
                      "-est actuellement classé {}er/ème\n".format(
                       players[number].get("Prenom"),
                       players[number].get("Nom"),
                       players[number].get("Elo"),
                       players[number].get("Point"),
                       number + 1))


"""        
        for player in range(x):
            print("\n---Joueur {} {}---\n"
                  "-a un elo de {}\n"
                  "-a {} point(s)\n"
                  "-est actuellement classé {}er/ème\n".format(
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Elo"),
                   players[player].get("Point"),
                   player + 1))
"""

test = LoadRoundData()
print(test.see_round_1())
