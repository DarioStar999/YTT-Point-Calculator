# HOW TO USE
# 1 - estrapolare dati con script da scrap_coral_stats.js nella console di chrome / browser generico
# 2 - copiare json che esce dalla console e metterlo in stats.json
# 3 - selezionare se si vuole direttamenti i punti o magari anche le altre statistiche (True o False in instaP)
# 4 - selezionare se si vuole avere i punti in json a parte (extracted.json) in jsonExtract
# 5(OPZIONALE) - inserire punti in killP bedP e FinalKillP

import json

with open("stats.json", "r", encoding="utf-8") as Fstats:
    data = json.load(Fstats)

instaP = True
jsonExtract = False
killP, bedP, FinalKillP = 5, 40, 25
punteggi = {}

for player in data:
    team = player["team"]
    username = player["username"]
    kill = int(player["kill"])
    letti_rotti = int(player["lettiRotti"])
    final_kill = int(player["finalKill"])

    if team not in punteggi:
        punteggi[team] = {
            "kill": 0,
            "lettiRotti": 0,
            "finalKill": 0,
            "players": []
        }

    punteggi[team]["kill"] += kill
    punteggi[team]["lettiRotti"] += letti_rotti
    punteggi[team]["finalKill"] += final_kill
    punteggi[team]["players"].append(username)

for team, stats in punteggi.items():
    players_str = ", ".join(stats["players"])
    totalP = (killP*int(stats["kill"])) + (bedP*int(stats["lettiRotti"])) + (FinalKillP*int(stats["finalKill"]))
    if instaP == False:
        print(f"Team {team}: kill = {stats['kill']}, bed = {stats['lettiRotti']}, Fkill = {stats['finalKill']}")
        print(f"Players: {players_str}, punti: {totalP}")
    else:
        print(f"{players_str}: {totalP}")
    if jsonExtract == True:
        dataExtract = {"players": stats["players"], "totalP": totalP}
        with open("extracted.json", "a", encoding="utf-8") as Fextract:
            json.dump(dataExtract, Fextract, indent=4)