import json


class Tournament1:

    def __init__(self):
        pass

    @staticmethod
    def tournament_1_question():

        tournaments = T1Data.load_tournament_data()
        t1 = tournaments[0]
        t1_rounds = int(t1["Nombre de rounds"])

        for rounds in range(t1_rounds):
            try:
                if t1_rounds == 1:
                    for_1_round = input(f"Quel round voulez-vous instancier ?\n"
                                        f"1 - Round n°{rounds + 1} ?"
                                        "Out - Revenir au menu\n"
                                        "Entrez votre choix : ")
                    return for_1_round

                elif t1_rounds == 2:
                    for_2_round = input(f"Quel round voulez-vous instancier ?\n"
                                        f"1 - Round n°{rounds + 1} ?\n"
                                        f"2 - Round n°{rounds + 2} ?\n"
                                        "Out - Revenir au menu\n"
                                        "Entrez votre choix : ")
                    return for_2_round

                elif t1_rounds == 3:
                    for_3_round = input(f"Quel round voulez-vous instancier ?\n"
                                        f"1 - Round n°{rounds + 1} ?\n"
                                        f"2 - Round n°{rounds + 2} ?\n"
                                        f"3 - Round n°{rounds + 3} ?\n"
                                        "Out - Revenir au menu\n"
                                        "Entrez votre choix : ")
                    return for_3_round

                elif t1_rounds == 4:
                    for_4_round = input(f"Quel round voulez-vous instancier ?\n"
                                        f"1 - Round n°{rounds + 1} ?\n"
                                        f"2 - Round n°{rounds + 2} ?\n"
                                        f"3 - Round n°{rounds + 3} ?\n"
                                        f"4 - Round n°{rounds + 4} ?\n"
                                        "Out - Revenir au menu\n"
                                        "Entrez votre choix : ")
                    return for_4_round

            except ValueError:
                print("ERREUR")

    def tournament_1_answer(self):

        question = self.tournament_1_question()
        print(question)

        try:
            if question == "1":
                T1Round1().point_distribution()
                self.tournament_1_answer()

            elif question == "Out":
                return

            elif question == "2" or "3" or "4":
                T1OtherRounds().point_distribution()
                self.tournament_1_answer()

            elif question != "1" or "2" or "3" or "4" or "Out":
                print("ERREUR : réponse non valable")
                self.tournament_1_answer()

        except ValueError:
            print("ERREUR : réponse non valable")
            self.tournament_1_answer()


class T1Data:

    def __init__(self):
        pass

    @staticmethod
    def load_tournament_data():

        with open("data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments

    @staticmethod
    def load_players_data():

        with open("data/player_data.json") as f:
            players = json.loads(f.read())

            return players

    def load_player_name(self):

        player_name = []

        players = self.load_players_data()
        for player in players:
            player_name.append(player["Prenom"])

        return player_name

    def load_player_tournament_data(self):

        with open(f"data/{self.clean_tournament_name()}/player_data_{self.clean_tournament_name()}.json") as f:
            players = json.loads(f.read())

            return players

    def clean_tournament_name(self):

        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            name = tournament["Nom"]
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


class T1Round1:

    def __init__(self):
        pass

    @staticmethod
    def tri_player_by_elo():
        """Tri par point elo"""

        data = T1Data.load_players_data()

        return sorted(data, key=lambda x: x["Elo"])

    def elo_pair(self):

        pairs = []
        player_list = self.tri_player_by_elo()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1

        return pairs

    def result_round(self):
        """Round 1 results"""

        winner = []
        loser = []
        equality = []
        a = 0
        b = 1
        c = 0
        print("Voici la liste des matchs : ")
        for x in range(len(self.elo_pair())):
            players_pair = self.elo_pair()[c]
            player_1 = players_pair[a]
            player_2 = players_pair[b]
            nom_player_1 = player_1["Prenom"]
            nom_player_2 = player_2["Prenom"]

            print(f"---Match {x + 1}---\n"
                  f"{nom_player_1} "
                  f"vs "
                  f"{nom_player_2}")

            user_input = input("Entrez le nom du vainqueur.\n"
                               "Si nul, entrez 'NUL'.\n"
                               "Résultat : ")

            try:
                if user_input == nom_player_1:
                    winner.append(nom_player_1)
                    loser.append(nom_player_2)

                elif user_input == nom_player_2:
                    winner.append(nom_player_2)
                    loser.append(nom_player_1)

                elif user_input == "NUL":
                    equality.append(nom_player_1)
                    equality.append(nom_player_2)

                else:
                    print("Réponse non valide, entrez le prénom du gagant ou entrez 'NUL' si nul")
                    self.result_round()

            except ValueError:
                print("Réponse non valide, entrez le prénom du gagant ou entrez 'NUL' si nul")
                self.result_round()

            c += 1

        round_1_result = {"Victoire": winner, "Défaite": loser, "Égalité": equality}

        return round_1_result

    def point_distribution(self):
        """Distribution des points"""

        result_match = self.result_round()
        all_players = T1Data().load_players_data()

        for player in all_players:
            if player["Prenom"] in result_match["Victoire"]:
                player["Point"] += 1

            elif player["Prenom"] in result_match["Défaite"]:
                player["Point"] += 0

            elif player["Prenom"] in result_match["Égalité"]:
                player["Point"] += 0.5

        tournaments = T1Data().clean_tournament_name()

        with open(f"data/{tournaments}/{tournaments}_1.json", "w") as f:
            json.dump(all_players, f, indent=2)

        with open(f"data/{tournaments}/player_data_{tournaments}.json", "w") as d:
            json.dump(all_players, d, indent=2)


class T1OtherRounds:

    def __init__(self):
        pass

    @staticmethod
    def tri_player_by_point():
        """Tri par point compétion"""

        data = T1Data().load_player_tournament_data()

        return sorted(data, key=lambda x: x["Point"])

    def point_pair(self):

        pairs = []
        player_list = self.tri_player_by_point()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1
        return pairs

    def result_round(self):
        """Other rounds results"""

        winner = []
        loser = []
        equality = []
        a = 0
        b = 1
        c = 0
        print("Voici la liste des matchs : ")
        for x in range(len(self.point_pair())):
            players_pair = self.point_pair()[c]
            player_1 = players_pair[a]
            player_2 = players_pair[b]
            nom_player_1 = player_1["Prenom"]
            nom_player_2 = player_2["Prenom"]

            print(f"---Match {x + 1}---\n"
                  f"{nom_player_1} "
                  f"vs "
                  f"{nom_player_2}")

            user_input = input("Entrez le nom du vainqueur.\n"
                               "Si nul, entrez 'NUL'.\n"
                               "Résultat : ")

            try:
                if user_input == nom_player_1:
                    winner.append(nom_player_1)
                    loser.append(nom_player_2)

                elif user_input == nom_player_2:
                    winner.append(nom_player_2)
                    loser.append(nom_player_1)

                elif user_input == "NUL":
                    equality.append(nom_player_1)
                    equality.append(nom_player_2)

                else:
                    print("Réponse non valide, entrez le prénom du gagant ou entrez 'NUL' si nul")
                    self.result_round()

            except ValueError:
                print("Réponse non valide, entrez le prénom du gagant ou entrez 'NUL' si nul")
                self.result_round()

            c += 1

        round_1_result = {"Victoire": winner, "Défaite": loser, "Égalité": equality}

        return round_1_result

    def point_distribution(self):
        """Distribution des points"""

        result_match = self.result_round()
        all_players = T1Data().load_player_tournament_data()

        for player in all_players:
            if player["Prenom"] in result_match["Victoire"]:
                player["Point"] += 1

            elif player["Prenom"] in result_match["Défaite"]:
                player["Point"] += 0

            elif player["Prenom"] in result_match["Égalité"]:
                player["Point"] += 0.5

        tournaments = T1Data().clean_tournament_name()
        x = 2

        try:
            with open(f"data/{tournaments}/{tournaments}_{x}.json") as f:
                players = json.loads(f.read())

                if len(players) == 0:
                    with open(f"data/{tournaments}/{tournaments}_{x}.json", "w") as e:
                        json.dump(all_players, e, indent=2)

                elif len(players) > 0:
                    x += 1

        except ValueError:
            print("WTFFFF")

        with open(f"data/{tournaments}/player_data_{tournaments}.json", "w") as d:
            json.dump(all_players, d, indent=2)


tournament1 = Tournament1()
# tournament1.tournament_1_question()
# tournament1.tournament_1_answer()

t1round1 = T1Round1()
# print(f"tri_player_by_elo() = {t1round1.tri_player_by_elo()}")
# print(f"elo_pair() = {t1round1.elo_pair()}")
# t1round1.elo_pair_to_json()
# print(f"result_round() = {t1round1.result_round()}")
# t1round1.point_distribution()

other_rounds = T1OtherRounds()
# print(f"tri_player_by_point() = {other_rounds.tri_player_by_point()}")
# print(f"point_pair() = {other_rounds.point_pair()}")
# other_rounds.point_pair_to_json()

# point_distribution = PointDistribution()
# point_distribution.result_round()
# print(point_distribution.list_for_point_distribution())
# point_distribution.point_distribution()
