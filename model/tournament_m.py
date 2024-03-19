class TournamentModel:

    def __init__(self, t_name, t_place, t_start, t_end, t_round_number, t_round_list, t_player_list, t_jury_remark):
        """define a tournament"""

        self.name = t_name
        self.place = t_place
        self.start = t_start
        self.end = t_end
        self.round_number = t_round_number
        self.round_list = t_round_list
        self.player_list = t_player_list
        self.jury_remark = t_jury_remark
