import json

from view.review_v import ReviewView


class ReviewController:
    """Data access"""

    def __init__(self):
        pass

    def general_responses(self):

        user_input = ReviewView().general_information()

        try:
            if user_input == "1":
                """Call fonction to see a player's result"""
                self.player_result()
                self.general_responses()

            elif user_input == "2":
                """Call fonction to see round 1 results"""
                print(self.all_rounds_result())
                self.general_responses()

            elif user_input == "3":
                """Pass to end the tournament"""
                print("Le tournois est terminé !")
                pass

            elif user_input != "1" or "2" or "3":
                print("ERREUR : Votre réponse n'est pas valable.")
                self.general_responses()

        except TypeError or ValueError:
            print(f"Votre réponse n'est pas valable, tapez 1, 2, 3, 4, 5 ou 6 {self.general_responses()}")

    @staticmethod
    def load_tournament_data():
        with open("../data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments


class ReviewT1:

    def __init__(self):
        pass

    @staticmethod
    def clean_tournament_1():

        tournaments = ReviewController.load_tournament_data()[0]

        name = tournaments["Nom"]
        lower_name = name.lower()
        cleaner_name = (lower_name
                        .replace(" ", "_")
                        .replace("'", "_")
                        .replace("-", "_")
                        .replace(".", "")
                        .replace("é", "e")
                        .replace("è", "e")
                        .replace("ê", "e")
                        .replace("ô", "o")
                        .replace("à", "a")
                        .replace("â", "a"))

        return cleaner_name

    def load_tournament_1(self):

        with open(f"../data/{self.clean_tournament_1()}/player_data_{self.clean_tournament_1()}.json") as f:
            players = json.loads(f.read())

            return players

    def print_tournament_1(self):

        players = self.load_tournament_1()

        print(f"\n====={self.clean_tournament_1()}=====")
        for number in range(len(players)):
            print("\n---{}er/ème - {} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   number + 1,
                   players[number].get("Prenom"),
                   players[number].get("Nom"),
                   players[number].get("Date de naissance"),
                   players[number].get("ID"),
                   players[number].get("Elo"),
                   players[number].get("Point")))


class ReviewT2:

    def __init__(self):
        pass

    @staticmethod
    def clean_tournament_2():

        tournaments = ReviewController.load_tournament_data()[1]

        name = tournaments["Nom"]
        lower_name = name.lower()
        cleaner_name = (lower_name
                        .replace(" ", "_")
                        .replace("'", "_")
                        .replace("-", "_")
                        .replace(".", "")
                        .replace("é", "e")
                        .replace("è", "e")
                        .replace("ê", "e")
                        .replace("ô", "o")
                        .replace("à", "a")
                        .replace("â", "a"))

        return cleaner_name

    def load_tournament_2(self):

        with open(f"../data/{self.clean_tournament_2()}/player_data_{self.clean_tournament_2()}.json") as f:
            players = json.loads(f.read())

            return players

    def print_tournament_2(self):

        players = self.load_tournament_2()

        print(f"\n====={self.clean_tournament_2()}=====")
        for number in range(len(players)):
            print("\n---{}er/ème - {} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   number + 1,
                   players[number].get("Prenom"),
                   players[number].get("Nom"),
                   players[number].get("Date de naissance"),
                   players[number].get("ID"),
                   players[number].get("Elo"),
                   players[number].get("Point")))


class ReviewT3:

    def __init__(self):
        pass

    @staticmethod
    def clean_tournament_3():

        tournaments = ReviewController.load_tournament_data()[2]

        name = tournaments["Nom"]
        lower_name = name.lower()
        cleaner_name = (lower_name
                        .replace(" ", "_")
                        .replace("'", "_")
                        .replace("-", "_")
                        .replace(".", "")
                        .replace("é", "e")
                        .replace("è", "e")
                        .replace("ê", "e")
                        .replace("ô", "o")
                        .replace("à", "a")
                        .replace("â", "a"))

        return cleaner_name

    def load_tournament_3(self):

        with open(f"../data/{self.clean_tournament_3()}/player_data_{self.clean_tournament_3()}.json") as f:
            players = json.loads(f.read())

            return players

    def ranking_result(self):
        # see ranking of all players

        result = self.load_tournament_3()

        return reversed(sorted(result, key=lambda x: x["Point"]))

    def print_tournament_3(self):

        players = self.ranking_result()

        print(f"\n====={self.clean_tournament_3()}=====")
        for number in range(len(self.load_tournament_3())):
            print("\n---{}er/ème - {} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   number + 1,
                   players[number].get("Prenom"),
                   players[number].get("Nom"),
                   players[number].get("Date de naissance"),
                   players[number].get("ID"),
                   players[number].get("Elo"),
                   players[number].get("Point")))


resume_controller = ReviewController()

t1 = ReviewT1()
t1.print_tournament_1()

t2 = ReviewT2()
t2.print_tournament_2()

t3 = ReviewT3()
t3.print_tournament_3()
