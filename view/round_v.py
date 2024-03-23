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
