class MenuView:
    """ask for what th user want to"""

    @staticmethod
    def menu_questions():

        print("\n==========MENU GÉNÉRAL==========\n")

        user_input = input("Bienvenue dans notre programme de création de tournoi, "
                           "que voulez-vous faire ? \n"
                           "1 - Créer/modifier la fiche d'un joueur\n"
                           "2 - Créer/modifier un tournois\n"
                           "3 - Créer/modifier des matchs\n"
                           "4 - Arreter le programme\n"
                           "Sélectionnez 1, 2, 3 ou 4 : ")

        return user_input
