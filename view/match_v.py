import json


class MatchView:

    def __init__(self):
        pass

    @staticmethod
    def match_questions():
        """Ask for what the user want to for their matchs and rounds"""

        print("\n==========INSTANCIATION DES MATCHS==========\n")

        user_input = input("Ici vous avez la main sur l'évolution des matchs de chaque tournoi.\n"
                           "Que voulez-vous faire ?\n"
                           "1 - Voir le classement des joueurs par elo,\n"
                           "2 - Voir le classement des joueurs par point de compétition,\n"
                           "3 - Entrer les résultats des tournois,\n"
                           "4 - Retourner au menu\n"

                           "Entrez 1, 2, 3 ou 4 : ")

        return user_input
