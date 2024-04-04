from view.match_v import MatchView
from controller.round_c import RoundController
from data.load_data_match import LoadPlayerData


class MatchController:

    def __init__(self):
        pass

    def match_answer(self):

        try:
            while 1:
                answer = MatchView.match_questions()

                if answer == "1":
                    LoadPlayerData.list_player_by_elo()
                    self.match_answer()

                elif answer == "2":
                    LoadPlayerData.list_player_by_point()
                    self.match_answer()

                elif answer == "3":
                    self.call_round_c()

                elif answer == "4":
                    """Retourner au menu"""
                    return

                elif answer != "1" or "2" or "3":
                    print("ERREUR : Votre réponse n'est pas valable.")
                    self.match_answer()

        except TypeError or ValueError:
            print("ERREUR : Votre réponse n'est pas valable.")
            self.match_answer()

    @staticmethod
    def call_round_c():

        round_c = RoundController()

        return round_c.pre_round_answer()


test = MatchController()
# test.match_answer()
