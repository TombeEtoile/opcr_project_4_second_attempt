import json


class RoundView:

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
    def tournament_with_1_round_questions():
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========INSTANCIATION DES ROUNDS==========\n")

        user_input = input("Ici vous avez la main sur l'évolution du round du tournoi.\n"
                           "Que voulez-vous faire ?\n"
                           "---Round n°1---\n"
                           "1 - Inscrire les résultats\n"
                           "2 - Voir les résultats\n"
                           "3 - Modifier les résultats\n"
                           "---Option menu---\n"
                           "4 - Revenir à l'étape suivante\n"
                           "Entrez votre choix : ")

        return user_input

    @staticmethod
    def tournament_with_2_rounds_questions():
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========INSTANCIATION DES ROUNDS==========\n")

        user_input = input("Ici vous avez la main sur l'évolution des rounds du tournoi.\n"
                           "Que voulez-vous faire ?\n"
                           "---Round n°1---\n"
                           "1 - Inscrire les résultats\n"
                           "2 - Voir les résultats\n"
                           "3 - Modifier les résultats\n"
                           "---Round n°2---\n"
                           "4 - Inscrire les résultats\n"
                           "5 - Voir les résultats\n"
                           "6 - Modifier les résultats\n"
                           "---Option menu---\n"
                           "7 - Revenir à l'étape suivante\n"
                           "Entrez votre choix : ")

        return user_input

    @staticmethod
    def tournament_with_3_rounds_questions():
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========INSTANCIATION DES ROUNDS==========\n")

        user_input = input("Ici vous avez la main sur l'évolution des rounds du tournoi.\n"
                           "Que voulez-vous faire ?\n"
                           "---Round n°1---\n"
                           "1 - Inscrire les résultats\n"
                           "2 - Voir les résultats\n"
                           "3 - Modifier les résultats\n"
                           "---Round n°2---\n"
                           "4 - Inscrire les résultats\n"
                           "5 - Voir les résultats\n"
                           "6 - Modifier les résultats\n"
                           "---Round n°3---\n"
                           "7 - Inscrire les résultats\n"
                           "8 - Voir les résultats\n"
                           "9 - Modifier les résultats\n"
                           "---Option menu---\n"
                           "10 - Revenir à l'étape suivante\n"
                           "Entrez votre choix : ")

        return user_input

    @staticmethod
    def tournament_with_4_rounds_questions():
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========INSTANCIATION DES ROUNDS==========\n")

        user_input = input("Ici vous avez la main sur l'évolution des rounds du tournoi.\n"
                           "Que voulez-vous faire ?\n"
                           "---Round n°1---\n"
                           "1 - Inscrire les résultats\n"
                           "2 - Voir les résultats\n"
                           "3 - Modifier les résultats\n"
                           "---Round n°2---\n"
                           "4 - Inscrire les résultats\n"
                           "5 - Voir les résultats\n"
                           "6 - Modifier les résultats\n"
                           "---Round n°3---\n"
                           "7 - Inscrire les résultats\n"
                           "8 - Voir les résultats\n"
                           "9 - Modifier les résultats\n"
                           "---Round n°3---\n"
                           "10 - Inscrire les résultats\n"
                           "11 - Voir les résultats\n"
                           "12 - Modifier les résultats\n"
                           "---Option menu---\n"
                           "13 - Revenir à l'étape suivante\n"
                           "Entrez votre choix : ")

        return user_input

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
