class Team:
    ZJUNLICT = "ZJUNlict"
    ROBODRAGONS = "RoboDragons"
    LUHBOTS = "Luhbots"
    ERFORCE = "ER-Force"
    KIKS = "KIKS"
    TIGERS = "TIGERs Mannheim"
    RTT = "RoboTeam Twente"
    TEAM_X = "Team X"
    TEAM_Y = "Team Y"

def load_2024_tournament():
    # """ 2024 TOURNAMENT """
    TEAMS_CYCLE = [Team.ERFORCE, Team.LUHBOTS, Team.KIKS, Team.RTT, Team.TIGERS, Team.ROBODRAGONS, Team.ZJUNLICT]

    # Match schedule here https://docs.google.com/spreadsheets/d/1wFbCYw-gfPdE7WykX31WSTPAvU3SWHysxapoCXWekbA/edit?gid=1087321196#gid=1087321196
    # Score sheet    here https://docs.google.com/spreadsheets/d/1KiqHZhVfNrZQpCc0nftIHPvuw9C-P_diZZ-TQojkGdM/edit?gid=1863286970#gid=1863286970
    MATCHES = [
        [Team.ERFORCE, Team.LUHBOTS, 9, 4],
        [Team.ZJUNLICT, Team.ROBODRAGONS, 67, 0],
        [Team.RTT, Team.TIGERS, 5, 52],
        [Team.KIKS, Team.RTT, 5, 17],
        [Team.TIGERS, Team.ROBODRAGONS, 65, 1],
        [Team.ERFORCE, Team.ZJUNLICT, 5, 11],
        [Team.KIKS, Team.LUHBOTS, 7, 10]
    ]

    # ER-Force 9 - 4 LUHBots 10 - 7 KIKS 5 - 17 RTT 5 - 52 TIGERs Mannheim 65 - 1 RoboDragons 0 - 67 ZJUNlict 11 - 5 ER-Force

    # TEAM            - TOTAL PASSES   ORIGINAL RANK       RANK WITH THIS SYSTEM       RESULT
    # ER-Force        - 14 passes      4th place shared    3rd place                   Moved up
    # LUHBots         - 14 passes      4th place shared    4th place
    # KIKS            - 12 passes      6th place           6th place
    # RoboTeam Twente - 22 passes      3rd place           5th place                   Dropped down
    # TIGERs Mannheim - 117 passes     1st place           1st place
    # RoboDragons     -   1 pass       7th place           7th place
    # ZJUNlict        - 78 passes      2nd place           2nd place

    return TEAMS_CYCLE, MATCHES

def load_example_tournament():
    """ EXAMPLE TOURNAMENT """
    TEAMS_CYCLE = [Team.ERFORCE, Team.TIGERS, Team.TEAM_X, Team.TEAM_Y, Team.ZJUNLICT]

    MATCHES = [
        [Team.ZJUNLICT, Team.ERFORCE, 5, 2],
        [Team.ERFORCE, Team.TIGERS, 4, 1],
        [Team.TIGERS, Team.TEAM_X, 45, 3],
        [Team.TEAM_X, Team.TEAM_Y, 8, 11],
        [Team.TEAM_Y, Team.ZJUNLICT, 12, 50]
    ]

    # ZJUNLict    - 55 passes total
    # ER-Force    -  6 passes total
    # TIGERS      - 46 passes total
    # TEAM_X      - 11 passes total
    # TEAM_Y      - 23 passes total

    ## Ranking based on total amount of passes:
    # ZJUNLict > TIGERS > TEAM_Y > TEAM_X > ER-Force
    # This makes no sense since ER-Force won against TIGERS and basically tied with ZJUNLict

    return TEAMS_CYCLE, MATCHES
