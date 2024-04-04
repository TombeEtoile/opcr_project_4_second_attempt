import json

from view.round_v import RoundView
from controller.rounds_c.tournament_1 import Tournament1
from controller.rounds_c.tournament_2 import Tournament2
from controller.rounds_c.tournament_3 import Tournament3


class RoundController:

    def __init__(self):
        pass

    def pre_round_answer(self):

        answer = RoundView().pre_round_questions()

        tournament = self.load_tournament_name()
        all_tournaments = int(len(self.load_tournament_name())) - int(len(self.load_tournament_name()))

        try:
            if answer == tournament[all_tournaments]:
                print(f"Vous avez selectionné le tournoi '{tournament[0]}'")
                Tournament1().tournament_1_answer()

            elif answer == tournament[all_tournaments + 1]:
                print(f"Vous avez selectionné le tournoi '{tournament[1]}'")
                Tournament2().tournament_2_answer()

            elif answer == tournament[all_tournaments + 2]:
                print(f"Vous avez selectionné le tournoi '{tournament[2]}'")
                Tournament3().tournament_3_answer()

            else:
                print("ERREUR : Votre réponse n'est pas valable.")
                self.pre_round_answer()

        except ValueError:
            print("ERREUR : Votre réponse n'est pas valable.")
            self.pre_round_answer()

    @staticmethod
    def load_tournament_data():

        with open("data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments

    def load_tournament_name(self):

        tournaments_name = []

        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            tournaments_name.append(tournament["Nom"])

        return tournaments_name
