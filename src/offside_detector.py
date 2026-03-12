def detect_offside(players):
    if len(players) < 3:
        return False, None
    players_sorted = sorted(players, key=lambda x: x[0])
    second_last_defender = players_sorted[-2]
    attacker = players_sorted[-1]
    defender_x = second_last_defender[0]
    attacker_x = attacker[0]
    if attacker_x > defender_x:
        return True, defender_x
    return False, defender_x