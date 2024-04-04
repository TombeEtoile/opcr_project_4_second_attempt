import json

from view.player_v import PlayerView, PlayerInstantiate


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
                self.list_all_players()

            elif response == "3":
                """modify player list"""
                self.edit_player()
                self.player_answer()

            elif response == "4":
                """delete player in the list"""
                self.delete_player()
                self.player_answer()

            elif response == "5":
                """Return to menu"""
                return

            elif response != "1" or "2" or "3" or "4" or "5":
                print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
                self.player_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
            self.player_answer()

    @staticmethod
    def load_player_data():

        with open("data/player_data.json") as f:
            players = json.loads(f.read())

            return players

    def add_player(self):

        new_player = PlayerInstantiate.get_player_data()

        with open("data/player_data.json", "ab+") as f:
            if f.tell() == 2:
                f.seek(-2, 2)
                f.truncate()
                f.write(b'[\n')
            else:
                f.seek(-2, 2)
                f.truncate()
                f.write(b',\n')
            f.write(json.dumps(new_player, indent=2).encode())
            f.write(b'\n]')

        self.player_answer()

    def list_all_players(self):

        players = self.load_player_data()
        print(players)
        for number in range(len(players)):
            print("\n---Joueur n°{} - {} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   number + 1,
                   players[number].get("Prenom"),
                   players[number].get("Nom"),
                   players[number].get("Date de naissance"),
                   players[number].get("ID"),
                   players[number].get("Elo"),
                   players[number].get("Point")))

        self.player_answer()

    def edit_player(self):

        print("Quel joueur voulez-vous modifier parmis la liste ci-dessous :")
        players = self.load_player_data()
        x = 1
        y = 1
        z = 1

        for player in players:
            print(f"{x} - {player["Prenom"]}")
            x += 1

        what_player = int(input("Entrez le numéro associé au joueur à modifier : "))

        print("---Fiche du joueur---")
        for cle, valeur in players[what_player - 1].items():
            print(f"{y} - {cle}: {valeur}")
            y += 1

        what_data = input("Quelle donnée voulez-vous modifier parmis la liste ci-dessus : ")
        new_data = input("Quelle nouvelle donnée voulez-vous afficher : ")

        print(players[what_player - 1])
        for data_test in players[what_player - 1].items():

            try:
                if what_data == "1":
                    change_player = players[what_player - 1]
                    change_player["Prenom"] = new_data
                elif what_data == "2":
                    change_player = players[what_player - 1]
                    change_player["Nom"] = new_data
                elif what_data == "3":
                    change_player = players[what_player - 1]
                    change_player["Date de naissance"] = new_data
                elif what_data == "4":
                    change_player = players[what_player - 1]
                    change_player["Elo"] = new_data
                elif what_data == "5":
                    change_player = players[what_player - 1]
                    change_player["ID"] = new_data
                elif what_data == "6":
                    change_player = players[what_player - 1]
                    change_player["Point"] = new_data
            except ValueError:
                print("ValueError")

        with open("data/player_data.json", "w") as f:
            json.dump(players, f, indent=2)
            f.flush()

    def delete_player(self):

        print("Quel joueur voulez-vous modifier parmis la liste ci-dessous :")

        players = self.load_player_data()
        x = 1
        y = 1

        for player in players:
            print(f"{x} - {player["Prenom"]}")
            x += 1

        player_to_remove = int(input("Entrez le numéro associé au joueur à supprimer de la liste : "))

        del players[player_to_remove - 1]

        print("---Le joueur a bien été supprimé de la liste, voici la nouvelle liste---")

        for player in players:
            print(f"{y} - {player["Prenom"]}")
            y += 1

        with open("data/player_data.json", "w") as f:
            json.dump(players, f, indent=2)
            f.flush()


test = PlayerController()
# test.player_answer()
# test.add_player()
# test.list_all_players()
