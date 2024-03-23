from view.menu_v import MenuView
from controller.tournament_c import TournamentController
from controller.player_c import PlayerController
from controller.match_c import MatchController


class MenuController:
    """Directs the user to the section of their choice"""

    def __init__(self):
        pass

    def menu_answer(self):

        response = MenuView.menu_questions()

        try:
            if response == "1":
                self.call_player_c()

            elif response == "2":
                self.call_tournament_c()

            elif response == "3":
                self.call_match_c()

            elif response == "4":
                pass

            elif response != "1" or "2" or "3" or "4":
                print("ERREUR : Vous devez écrire 1, 2, 3 ou 4")
                self.menu_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2 ou 3")
            self.menu_answer()

    @staticmethod
    def call_player_c():

        player = PlayerController()

        return player.player_answer()

    @staticmethod
    def call_tournament_c():

        tournament = TournamentController()

        return tournament.tournament_answer()

    @staticmethod
    def call_match_c():

        match = MatchController()

        return match.match_answer()
