import json

from view.tournament_v import TournamentView, TournamentInstantiate


class TournamentController:

    def __init__(self):
        pass

    def tournament_answer(self):

        response = TournamentView.tournament_questions()

        try:
            if response == "1":
                """add tournament"""
                self.add_tournament()

            elif response == "2":
                """check list of tournament"""
                self.list_all_tournament()

            elif response == "3":
                """modify tournament list"""
                self.edit_tournament()
                self.tournament_answer()

            elif response == "4":
                """delete tournament in the list"""
                self.delete_tournament()
                self.tournament_answer()

            elif response == "5":
                """Return to menu"""
                return

            elif response != "1" or "2" or "3" or "4" or "5":
                print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
                self.tournament_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
            self.tournament_answer()

    @staticmethod
    def load_tournament_data():

        with open("data/tournament_data.json") as f:
            players = json.loads(f.read())

            return players

    def add_tournament(self):

        print(len(self.load_tournament_data()))
        new_tournament = TournamentInstantiate.get_tournament_data()

        try:
            if len(self.load_tournament_data()) < 3:
                with open("data/tournament_data.json", "ab+") as f:
                    if f.tell() == 2:
                        f.seek(-2, 2)
                        f.truncate()
                        f.write(b'[\n')
                    else:
                        f.seek(-2, 2)
                        f.truncate()
                        f.write(b',\n')
                    f.write(json.dumps(new_tournament, indent=2).encode())
                    f.write(b'\n]')
                self.tournament_answer()

            elif len(self.load_tournament_data()) > 2:
                print("Le nombre maximum de tournois est de 3.\n"
                      "Veuillez clôturer un tournoi avant d'en lancer un autre.")
                self.tournament_answer()

        except ValueError:
            print("Le nombre maximum de tournois est de 3.\n"
                  "Veuillez clôturer un tournoi avant d'en lancer un autre.")
            self.tournament_answer()

    def list_all_tournament(self):

        tournaments = self.load_tournament_data()
        for tournament in range(len(tournaments)):
            print("\n---Tournoi n°{} - {}---\n"
                  "-aura lieux en {}\n"
                  "-comencera le {} et finira le {}\n"
                  "-se déroulera en {} round(s).\n"
                  "-Remarque du jury : {}".format(
                   tournament + 1,
                   tournaments[tournament].get("Nom"),
                   tournaments[tournament].get("Lieu"),
                   tournaments[tournament].get("Date de début"),
                   tournaments[tournament].get("Date de fin"),
                   tournaments[tournament].get("Nombre de rounds"),
                   tournaments[tournament].get("Remarque du jury")))

        self.tournament_answer()

    def edit_tournament(self):

        print("Quel joueur voulez-vous modifier parmis la liste ci-dessous :")
        tournaments = self.load_tournament_data()
        x = 1
        y = 1

        for tournament in tournaments:
            print(f"{x} - {tournament["Nom"]}")
            x += 1

        what_tournament = int(input("Entrez le numéro associé au joueur à modifier : "))

        print("---Fiche du joueur---")
        for cle, valeur in tournaments[what_tournament - 1].items():
            print(f"{y} - {cle}: {valeur}")
            y += 1

        what_data = input("Quelle donnée voulez-vous modifier parmis la liste ci-dessus : ")
        new_data = input("Quelle nouvelle donnée voulez-vous afficher : ")

        print(tournaments[what_tournament - 1])
        for data_test in tournaments[what_tournament - 1].items():

            try:
                if what_data == "1":
                    change_tournament = tournaments[what_tournament - 1]
                    change_tournament["Nom"] = new_data
                elif what_data == "2":
                    change_tournament = tournaments[what_tournament - 1]
                    change_tournament["Lieu"] = new_data
                elif what_data == "3":
                    change_tournament = tournaments[what_tournament - 1]
                    change_tournament["Date de début"] = new_data
                elif what_data == "4":
                    change_tournament = tournaments[what_tournament - 1]
                    change_tournament["Date de fin"] = new_data
                elif what_data == "5":
                    change_tournament = tournaments[what_tournament - 1]
                    change_tournament["Nombre de rounds"] = new_data
                elif what_data == "6":
                    change_tournament = tournaments[what_tournament - 1]
                    change_tournament["Remarque du jury"] = new_data
            except ValueError:
                print("ValueError")

        with open("data/tournament_data.json", "w") as f:
            json.dump(tournaments, f, indent=2)

    def delete_tournament(self):

        print("Quel joueur voulez-vous modifier parmis la liste ci-dessous :")
        tournaments = self.load_tournament_data()
        x = 1
        y = 1
        z = 1

        for tournament in tournaments:
            print(f"{x} - {tournament["Nom"]}")
            x += 1

        player_to_remove = int(input("Entrez le numéro associé au joueur à supprimer de la liste : "))

        del tournaments[player_to_remove - 1]

        print("---Le joueur a bien été supprimé de la liste, voici la nouvelle liste---")

        for tournament in tournaments:
            print(f"{z} - {tournament["Nom"]}")
            z += 1

        with open("data/tournament_data.json", "w") as f:
            json.dump(tournaments, f, indent=2)


test = TournamentController()
# test.add_tournament()
