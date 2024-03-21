import json


class MatchView:

    def __init__(self):
        pass

    @staticmethod
    def match_questions():
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========INSTANCIATION DES ROUNDS==========\n")

        user_input = input("Ici vous avez la main sur l'évolution des matchs de chaque tournoi.\n"
                           "Que voulez-vous faire ?\n"
                           "1 - Voir le classement des joueurs par elo,\n"
                           "2 - Voir le classement des joueurs par point de compétition,\n"
                           "3 - Voir l'organisation du prochain round,\n"
                           "4 - Inscrire les résultats du round 1,\n "
                           "5 - Voir le classement des joueurs suite au round 1,\n"
                           "6 - Passer à l'inscription des rounds suivants\n"
                           "Entrez 1, 2, 3, 4 ou 5 : ")

        return user_input
