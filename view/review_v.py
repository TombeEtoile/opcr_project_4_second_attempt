import json


class ReviewView:

    def __init__(self):
        pass

    def general_information(self):
        """Menu choice"""

        tournament_1 = self.load_tournament_data()[0]
        tournament_2 = self.load_tournament_data()[1]
        tournament_3 = self.load_tournament_data()[2]
        x = 1

        print("Sélectionnez les données que vous souhaitez analyser : ")

        return input(f"1 - voir les résultats du tournois n°{x} - {tournament_1}\n"
                     f"2 - voir les résultats du tournois n°{x + 1} - {tournament_2} \n"
                     f"3 - voir les résultats du tournois n°{x + 2} - {tournament_3} \n"
                     "4 - Retourner au menu \n"
                     "Tapez 1, 2 ou 3 : ")

    @staticmethod
    def load_tournament_data():
        with open("../data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments


resume_view = ReviewView()
