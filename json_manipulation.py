import json


def player_data():
    """creat Json for players"""

    with open("player_data.json", "w+") as f:
        data = {}
        json.dump(data, f, indent=2)


def tournament_data():
    """creat Json for tournaments"""

    with open("tournament_data.json", "w+") as f:
        data = {}
        json.dump(data, f, indent=2)


# player_data()
# tournament_data()
