class MenuView:
    """ask for what th user want to"""

    @staticmethod
    def menu_questions():
        user_input = input("Bienvenue dans notre programme de création de tournoi, "
                           "que voulez-vous faire ? \n"
                           "1 - Créer/modifier la fiche d'un joueur\n"
                           "2 - Créer/modifier un tournois\n"
                           "3 - Arreter le programme\n"
                           "Sélectionnez 1, 2 ou 3 : ")

        return user_input


menu = MenuView
# menu.menu_questions()
