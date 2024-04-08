class TournamentView:

    @staticmethod
    def tournament_questions():
        """ask for what the user want to for his player"""

        print("\n==========INSTANCIATION D'UN TOURNOI==========\n")

        user_input = input("Ici vous pouvez agir sur chaque tournoi. "
                           "Que voulez-vous faire ? \n"
                           "1 - Ajouter\n"
                           "2 - Voir la liste des tournois\n"
                           "3 - Modifier\n"
                           "4 - Supprimer\n"
                           "5 - Retourner au menu\n"
                           "Sélectionnez 1, 2, 3, 4 ou 5 : ")

        return user_input


class TournamentInstantiate:
    """Creat a tournament"""

    @staticmethod
    def name():
        """Tournament name"""

        user_input = input("Entrez le nom du tournoi : ")

        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return TournamentInstantiate.name()

        except ValueError:
            return user_input

    @staticmethod
    def place():
        """Tournament place"""

        user_input = input("Entrez le pays dans lequel se déroule le tournoi : ")

        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return TournamentInstantiate.name()

        except ValueError:
            return user_input

    @staticmethod
    def day():
        """Tournament day of start/end"""

        user_input_1 = input("jj : ")

        try:
            if user_input_1 > "31":
                print("ERREUR : jour non valide")
                TournamentInstantiate.day()

            elif "0" < user_input_1 < "32":
                return user_input_1

        except ValueError:
            print("ERREUR : jour non valide")
            TournamentInstantiate.day()

    @staticmethod
    def month():
        """Tournament month of start/end"""

        user_input_2 = input("mm : ")

        try:
            if user_input_2 > "12":
                print("ERREUR : mois non valide")
                TournamentInstantiate.month()

            elif "0" < user_input_2 < "13":
                return user_input_2

        except ValueError:
            print("ERREUR : mois non valide")
            TournamentInstantiate.month()

    @staticmethod
    def year():
        """Tournament year of start/end"""

        user_input_3 = input("aaaa : ")

        try:
            if user_input_3 < "2024":
                print("ERREUR : année non valide")
                TournamentInstantiate.year()

            else:
                return user_input_3

        except ValueError:
            print("ERREUR : année non valide")
            TournamentInstantiate.year()

    @staticmethod
    def start():
        """Tournament start"""

        print("--- Date de début ---")

        return (f"{TournamentInstantiate.day()}/"
                f"{TournamentInstantiate.month()}/"
                f"{TournamentInstantiate.year()}")

    @staticmethod
    def end():
        """Tournament end"""

        print("--- Date de fin ---")

        return (f"{TournamentInstantiate.day()}/"
                f"{TournamentInstantiate.month()}/"
                f"{TournamentInstantiate.year()}")

    @staticmethod
    def round_number():
        """Tournament round number"""

        user_input = input("Nombre de rounds : ")

        try:
            if user_input == "0":
                print("ERREUR : le tournoi doit faire au moins 1 round")
                TournamentInstantiate.round_number()

            elif user_input > "4":
                print("ERREUR : le tournoi doit faire maximum 4 rounds")
                TournamentInstantiate.round_number()

            elif "0" < user_input < "5":
                return user_input

        except ValueError:
            print("ERREUR : donnée non valide, entrez un chiffre compris entre 1 et 4")
            TournamentInstantiate.round_number()

    @staticmethod
    def jury_remark():
        """Tournament jury remark"""

        user_input = input("Entrez votre remarque : ")

        return user_input

    @staticmethod
    def get_tournament_data():
        """Creat tournament profil"""

        name = TournamentInstantiate.name()
        place = TournamentInstantiate.place()
        start = TournamentInstantiate.start()
        end = TournamentInstantiate.end()
        round_number = TournamentInstantiate.round_number()
        jury_remark = TournamentInstantiate.jury_remark()

        tournament = {"Nom": name,
                      "Lieu": place,
                      "Date de début": start,
                      "Date de fin": end,
                      "Nombre de rounds": round_number,
                      "Remarque du jury": jury_remark}

        return tournament
