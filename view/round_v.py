import json


class PreRoundView:

    def __init__(self):
        pass

    def pre_round_questions(self):
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========CHOIX DU TOURNOIS À COMPLÉTER==========\n")

        user_input = input("Choisissez le tournoi que vous voulez compléter parmi cette liste :\n"
                           f"{self.load_tournament_name()}\n"
                           "Copiez-collez le tournoi de votre choix : ")

        return user_input

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


class RoundView:

    def __init__(self):
        pass

    @staticmethod
    def round_questions():
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========INSTANCIATION DES ROUNDS==========\n")

        user_input = input("Ici vous avez la main sur l'évolution des rounds de chaque tournoi.\n"
                           "Que voulez-vous faire ?\n"
                           "1 - Inscrire les résultats du round 1,\n"
                           "2 - Inscrire les résultats du round 2,\n"
                           "3 - Inscrire les résultats du round 3,\n"
                           "4 - Inscrire les résultats du round 4,\n"
                           "5 - Revenir à l'étape suivante\n"
                           "Entrez 1, 2, 3, 4 ou 5 : ")

        return user_input
