class PlayerModel:
    """define a player"""

    def __init__(self,
                 p_name=str,
                 p_surname=str,
                 p_birthday=str,
                 p_identifier=str,
                 p_elo=int,
                 p_point=int):

        self.name = p_name
        self.surname = p_surname
        self.birthday = p_birthday
        self.identifier = p_identifier
        self.elo = p_elo
        self.point = p_point
