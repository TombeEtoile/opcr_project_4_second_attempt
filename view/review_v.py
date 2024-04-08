import json


class ReviewView:

    def __init__(self):
        pass

    def general_information(self):
        """Menu choice"""

        try:
            if len(self.load_tournament_data()) == 1:
                tournament_1 = self.load_tournament_data()[0]
                x = 1

                print("Sélectionnez les données que vous souhaitez analyser : ")

                return input(f"1 - voir les résultats du tournois n°{x} - {tournament_1["Nom"]}\n"
                             "2 - Retourner au menu \n"
                             "Tapez 1 ou 2 : ")

            elif len(self.load_tournament_data()) == 2:
                tournament_1 = self.load_tournament_data()[0]
                tournament_2 = self.load_tournament_data()[1]
                x = 1

                print("Sélectionnez les données que vous souhaitez analyser : ")

                return input(f"1 - voir les résultats du tournois n°{x} - {tournament_1["Nom"]}\n"
                             f"2 - voir les résultats du tournois n°{x + 1} - {tournament_2["Nom"]} \n"
                             "3 - Retourner au menu \n"
                             "Tapez 1, 2 ou 3 : ")

            elif len(self.load_tournament_data()) == 3:

                tournament_1 = self.load_tournament_data()[0]
                tournament_2 = self.load_tournament_data()[1]
                tournament_3 = self.load_tournament_data()[2]
                x = 1

                print("Sélectionnez les données que vous souhaitez analyser : ")

                return input(f"1 - voir les résultats du tournois n°{x} - {tournament_1["Nom"]}\n"
                             f"2 - voir les résultats du tournois n°{x + 1} - {tournament_2["Nom"]} \n"
                             f"3 - voir les résultats du tournois n°{x + 2} - {tournament_3["Nom"]} \n"
                             "4 - Retourner au menu \n"
                             "Tapez 1, 2, 3 ou 4 : ")

        except ValueError:
            print("ERREUR : veuillez redémarrer le programme")
            self.general_information()

    @staticmethod
    def load_tournament_data():
        """Load tournament data"""

        with open("data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments


# test = ReviewView()
# test.general_information()
