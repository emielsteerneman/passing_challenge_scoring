import numpy as np

ZJUNLICT = "ZJUNlict"
ROBODRAGONS = "RoboDragons"
LUHBOTS = "Luhbots"
ERFORCE = "ER-Force"
KIKS = "KIKS"
TIGERS = "TIGERs Mannheim"
RTT = "RoboTeam Twente"





""" EXAMPLE TOURNAMENT """
TEAMS_CYCLE = [ERFORCE, LUHBOTS, KIKS, ROBODRAGONS, ZJUNLICT]

MATCHES = [
    [ZJUNLICT, ERFORCE, 3, 2],
    [ERFORCE, LUHBOTS, 2, 1],
    [LUHBOTS, KIKS, 45, 3],
    [KIKS, ROBODRAGONS, 8, 10],
    [ROBODRAGONS, ZJUNLICT, 12, 50]
]

# ZJUNLict    - 53 passes total
# ER-Force    -  5 passes total
# LUHBots     - 46 passes total
# KIKS        - 13 passes total
# RoboDragons - 22 passes total

## Ranking based on passes:
# ZJUNLict > LUHbots > RoboDragons > KIKS > ER-Force
# This makes no sense since ER-Force won against LUHBots and basically tied with ZJUNLict





""" 2024 TOURNAMENT """
TEAMS_CYCLE = [ERFORCE, LUHBOTS, KIKS, RTT, TIGERS, ROBODRAGONS, ZJUNLICT]

# Match schedule here https://docs.google.com/spreadsheets/d/1wFbCYw-gfPdE7WykX31WSTPAvU3SWHysxapoCXWekbA/edit?gid=1087321196#gid=1087321196
# Score sheet    here https://docs.google.com/spreadsheets/d/1KiqHZhVfNrZQpCc0nftIHPvuw9C-P_diZZ-TQojkGdM/edit?gid=1863286970#gid=1863286970
MATCHES = [
    [ERFORCE, LUHBOTS, 9, 4],
    [ZJUNLICT, ROBODRAGONS, 67, 0],
    [RTT, TIGERS, 5, 52],
    [KIKS, RTT, 5, 17],
    [TIGERS, ROBODRAGONS, 65, 1],
    [ERFORCE, ZJUNLICT, 5, 11],
    [KIKS, LUHBOTS, 7, 10]
]

# ER-Force 9 - 4 LUHBots 10 - 7 KIKS 5 - 17 RTT 5 - 52 TIGERs Mannheim 65 - 1 RoboDragons 0 - 67 ZJUNlict 11 - 5 ER-Force

# TEAM            - TOTAL PASSES        ORIGINAL RANK       RANK WITH THIS SYSTEM       RESULT
# ER-Force        - 14 passes total     4th place shared    3rd place                   Moved up
# LUHBots         - 14 passes total     4th place shared    4th place
# KIKS            - 12 passes total     6th place           6th place
# RoboTeam Twente - 22 passes total     3rd place           5th place                   Dropped down
# TIGERs Mannheim - 117 passes total    1st place           1st place
# RoboDragons     - 1 pass total        7th place           7th place
# ZJUNlict        - 78 passes total     2nd place           2nd place





def solve_spring_system(current:list[float], springs:list[float], step:float=0.01) -> list[float]:
    step = float(step) # Convert from np.float to python float
    n = len(current)
    new = current.copy()

    # For each team
    for i in range(n):
        i_left, i_right = (i-1+n)%n, (i+1)%n
        # Get the spring force between the current team and the team to the left and right
        spring_left, spring_right = -springs[i_left], springs[i]
        # Calculate the difference between the current state and the spring force
        diff_left, diff_right = (current[i] - current[i_left]), (current[i] - current[i_right])
        # Calculate the movement of the team based on the difference
        move_left, move_right = (spring_left - diff_left), (spring_right - diff_right)
        # Step the team based on the movement
        step_size = step * (move_left + move_right)
        new[i] += step_size

    return new





if __name__ == "__main__":

    get_total_passes = lambda matches, team: sum([ m[m.index(team)+2] for m in matches if team in m ])

    # Calculate total passes per team
    passes_per_team = { team: get_total_passes(MATCHES, team) for team in TEAMS_CYCLE }

    # Create initial state
    initial = [ 0. for team in TEAMS_CYCLE ]
    springs = []
    # For each team pair that played against each other, calculate the difference in passes
    for team1, team2 in zip(TEAMS_CYCLE, TEAMS_CYCLE[1:] + [TEAMS_CYCLE[0]]):
        # Find the match between the two teams
        match = [ m for m in MATCHES if team1 in m and team2 in m ][0]
        # Get the total passes for each team
        s1, s2 = match[match.index(team1)+2], match[match.index(team2)+2]
        # The difference in passes is the spring value. See drawing.drawio for more info
        springs.append(s1-s2)

    # Iteratively solve the spring system until it converges
    current = initial
    prev = [0.0] * len(TEAMS_CYCLE)

    for i in range(1000):
    
        current = solve_spring_system(current, springs, step=0.01 + 0.01*i)
    
        if np.allclose(current, prev, atol=0.0001):
            print(f"Scores converged at step {i}")
            break
    
        prev = current
    
    score_team = list(zip(current, TEAMS_CYCLE))
    for score, team in sorted(score_team, reverse=True):
        print(f"{team:<16} | {score:.2f}")