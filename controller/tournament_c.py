import json

from view.tournament_v import TournamentView, TournamentInstantiate
from data.load_data import LoadTournamentData


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
                """modify player list"""
                self.edit_tournament()

            elif response == "4":
                """delete player in the list"""
                self.delete_tournament()

            elif response == "5":
                """Return to menu"""
                self.return_to_menu()

            elif response != "1" or "2" or "3" or "4" or "5":
                print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
                self.tournament_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
            self.tournament_answer()

    def add_tournament(self):

        new_tournament = TournamentInstantiate.get_tournament_data()

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

    def list_all_tournament(self):

        tournaments = LoadTournamentData.load_tournament_data()
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
        pass

    def delete_tournament(self):
        pass

    def return_to_menu(self):
        pass
