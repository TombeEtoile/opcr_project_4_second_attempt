class TournamentModel:
    """define a tournament"""

    def __init__(self,
                 t_name=str,
                 t_place=str,
                 t_start=str,
                 t_end=str,
                 t_round_number=int,
                 t_round_list=int,
                 t_player_list=list,
                 t_jury_remark=str):

        self.name = t_name
        self.place = t_place
        self.start = t_start
        self.end = t_end
        self.round_number = t_round_number
        self.round_list = t_round_list
        self.player_list = t_player_list
        self.jury_remark = t_jury_remark
