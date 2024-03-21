import random
import string


class PlayerView:
    """ask for what the user want to for his player"""

    @staticmethod
    def player_questions():

        print("\n==========INSTANCIATION D'UN JOUEUR==========\n")

        user_input = input("Ici vous pouvez agir sur chaque joueur. "
                           "Que voulez-vous faire ? \n"
                           "1 - Ajouter\n"
                           "2 - Voir la liste des joueurs\n"
                           "3 - Modifier\n"
                           "4 - Supprimer\n"
                           "5 - Retourner au menu\n"
                           "Entrez 1, 2, 3, 4 ou 5 : ")

        return user_input


class PlayerInstantiate:
    """Creat a player"""

    @staticmethod
    def name():
        """Player name"""

        user_input = input("Entrez votre nom : ")

        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return PlayerInstantiate.name()

        except ValueError:
            return user_input

    @staticmethod
    def surname():
        """Player surname"""

        user_input = input("Entrez votre prénom : ")

        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return PlayerInstantiate.surname()

        except ValueError:
            return user_input

    @staticmethod
    def day():
        """Player day of birth"""

        user_input_1 = input("jj : ")

        try:
            if user_input_1 > "31":
                print("ERREUR : jour de naissance non valide")
                PlayerInstantiate.day()

            elif "0" < user_input_1 < "32":
                return user_input_1

        except ValueError:
            print("ERREUR : jour de naissance non valide")
            PlayerInstantiate.day()

    @staticmethod
    def month():
        """Player month of birth"""

        user_input_2 = input("mm : ")

        try:
            if user_input_2 > "12":
                print("ERREUR : mois de naissance non valide")
                PlayerInstantiate.month()

            elif "0" < user_input_2 < "13":
                return user_input_2

        except ValueError:
            print("ERREUR : mois de naissance non valide")
            PlayerInstantiate.month()

    @staticmethod
    def year():
        """Player year of birth"""

        user_input_3 = input("aaaa : ")

        try:
            if user_input_3 > "2020":
                print("ERREUR : année de naissance non valide")
                PlayerInstantiate.year()

            elif user_input_3 < "1924":
                print("ERREUR : année de naissance non valide")
                PlayerInstantiate.year()

            elif "1924" < user_input_3 < "1924":
                return user_input_3

        except ValueError:
            print("ERREUR : année de naissance non valide")
            PlayerInstantiate.year()

    @staticmethod
    def birthday():
        """Player's birthday"""

        return (f"{PlayerInstantiate.day()}/"
                f"{PlayerInstantiate.month()}/"
                f"{PlayerInstantiate.year()}")

    @staticmethod
    def elo():
        """player elo"""

        player_elo = random.randint(1800, 2200)

        return player_elo

    @staticmethod
    def identifier():
        """player ID"""

        player_id = (f"{random.randint(1000, 9999)}"
                     f"{random.choice(string.ascii_letters)}"
                     f"{random.choice(string.ascii_letters)}"
                     f"{random.choice(string.ascii_letters)}"
                     f"{random.randint(1000, 9999)}")

        return player_id

    @staticmethod
    def point():
        """Setting 0 point for all the players"""

        return 0

    @staticmethod
    def get_player_data():
        """Creat player profil"""

        print("---Ajout d'un joueur---\n")

        surname = PlayerInstantiate.surname()
        name = PlayerInstantiate.name()
        birthday = PlayerInstantiate.birthday()
        elo = PlayerInstantiate.elo()
        identifier = PlayerInstantiate.identifier()
        point = PlayerInstantiate.point()

        player = {"Prenom": surname,
                  "Nom": name,
                  "Date de naissance": birthday,
                  "Elo": elo,
                  "ID": identifier,
                  "Point": point}

        print(player)
        return player
