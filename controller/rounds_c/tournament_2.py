import json


class Tournament2:

    def __init__(self):
        pass

    @staticmethod
    def tournament_2_question():
        """user-selected routing from round_c"""

        tournaments = T2Data.load_tournament_data()
        t2 = tournaments[1]
        t2_rounds = int(t2["Nombre de rounds"])

        for rounds in range(t2_rounds):
            try:
                if t2_rounds == 1:
                    for_1_round = input(f"Quel round voulez-vous instancier ?\n"
                                        f"1 - Round n°{rounds + 1} ?"
                                        "Out - Revenir au menu\n"
                                        "Entrez votre choix : ")
                    return for_1_round

                elif t2_rounds == 2:
                    for_2_round = input(f"Quel round voulez-vous instancier ?\n"
                                        f"1 - Round n°{rounds + 1} ?\n"
                                        f"2 - Round n°{rounds + 2} ?\n"
                                        "Out - Revenir au menu\n"
                                        "Entrez votre choix : ")
                    return for_2_round

                elif t2_rounds == 3:
                    for_3_round = input(f"Quel round voulez-vous instancier ?\n"
                                        f"1 - Round n°{rounds + 1} ?\n"
                                        f"2 - Round n°{rounds + 2} ?\n"
                                        f"3 - Round n°{rounds + 3} ?\n"
                                        "Out - Revenir au menu\n"
                                        "Entrez votre choix : ")
                    return for_3_round

                elif t2_rounds == 4:
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

    def tournament_2_answer(self):
        """user-selected routing from tournament_2_questions"""

        question = self.tournament_2_question()

        try:
            if question == "1":
                T2Round1().point_distribution()
                self.tournament_2_answer()

            elif question == "Out":
                return

            elif question == "2" or "3" or "4":
                T2OtherRounds().point_distribution()
                self.tournament_2_answer()

            elif question != "1" or "2" or "3" or "4":
                print("ERREUR : réponse non valable")
                self.tournament_2_answer()

        except ValueError:
            print("ERREUR : réponse non valable")
            self.tournament_2_answer()


class T2Data:

    def __init__(self):
        pass

    @staticmethod
    def load_tournament_data():
        """tournament data"""

        with open("data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments

    @staticmethod
    def load_players_data():
        """Player data"""

        with open("data/player_data.json") as f:
            players = json.loads(f.read())

            return players

    def load_player_name(self):
        """Player data name"""

        player_name = []

        players = self.load_players_data()
        for player in players:
            player_name.append(player["Prenom"])

        return player_name

    def load_player_tournament_data(self):
        """Tournament data from tournament_2 folder"""

        with open(f"data/{self.clean_tournament_name()}/player_data_{self.clean_tournament_name()}.json") as f:
            players = json.loads(f.read())

            return players

    def clean_tournament_name(self):
        """Clean tournament 2 name"""

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


class T2Round1:

    def __init__(self):
        pass

    @staticmethod
    def tri_player_by_elo():
        """Players sorted by elo point"""

        data = T2Data.load_players_data()

        return sorted(data, key=lambda x: x["Elo"])

    def elo_pair(self):
        """Creat elo pair"""

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
        """Round 2 results"""

        winner = []
        loser = []
        equality = []
        a = 0
        b = 1
        c = 0
        print("Voici la liste des match : ")
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
        """Points distribution"""

        result_match = self.result_round()
        all_players = T2Data().load_players_data()

        for player in all_players:
            if player["Prenom"] in result_match["Victoire"]:
                player["Point"] += 1

            elif player["Prenom"] in result_match["Défaite"]:
                player["Point"] += 0

            elif player["Prenom"] in result_match["Égalité"]:
                player["Point"] += 0.5

        tournaments = T2Data().clean_tournament_name()

        with open(f"data/{tournaments}/{tournaments}_1.json", "w") as f:
            json.dump(all_players, f, indent=2)

        with open(f"data/{tournaments}/player_data_{tournaments}.json", "w") as d:
            json.dump(all_players, d, indent=2)


class T2OtherRounds:

    def __init__(self):
        pass

    @staticmethod
    def tri_player_by_point():
        """Players sorted by point"""

        data = T2Data().load_player_tournament_data()

        return sorted(data, key=lambda x: x["Point"])

    def point_pair(self):
        """Creat pari of players by point"""

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
        print("Voici la liste des match : ")
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
        """Points distribution"""

        result_match = self.result_round()
        all_players = T2Data().load_player_tournament_data()

        for player in all_players:
            if player["Prenom"] in result_match["Victoire"]:
                player["Point"] += 1

            elif player["Prenom"] in result_match["Défaite"]:
                player["Point"] += 0

            elif player["Prenom"] in result_match["Égalité"]:
                player["Point"] += 0.5

        tournaments = T2Data().clean_tournament_name()
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
            print("ERROR")

        with open(f"data/{tournaments}/player_data_{tournaments}.json", "w") as d:
            json.dump(all_players, d, indent=2)
