import cv2
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





def render(teams, springs, values, timeout=0):
    GRID_STEP = 3
    
    def show(image, timeout=0):
        cv2.imshow("image", image)
        if cv2.waitKey(timeout) == ord('q'):
            exit()

    image = np.zeros((800, 1200, 3), np.uint8)
    YCENTER = 4 * image.shape[0] // 5
    XSTEP = 1000 // len(teams)

    ### Draw grid
    for i in range(0, 140, 10):
        # Vertical
        cv2.line(image, (200*i, 0), (200*i, 1000), (50, 50, 50), 1)
        # Horizontal
        cv2.line(image, (0, YCENTER - i * GRID_STEP), (1200, YCENTER - i * GRID_STEP), (50, 50, 50), 1)
        cv2.line(image, (0, YCENTER + i * GRID_STEP), (1200, YCENTER + i * GRID_STEP), (50, 50, 50), 1)
    cv2.line(image, (0, YCENTER), (1200, YCENTER), (255, 255, 255), 1)
    
    ### Draw teams
    get_color = lambda i: (255 - i*50, 0, i*50)

    for i, (team, spring, value) in enumerate(zip(teams, springs, values)):
        x, y = 200+i*XSTEP, YCENTER-int(value*GRID_STEP)
        x2, y2 = 200+(i+1)*XSTEP, YCENTER-int(values[(i+1)%len(teams)]*GRID_STEP)

        ranking = sum([ v >= value for v in values ])
        cv2.circle(image, (x, y), 20, get_color(i), -1, cv2.LINE_AA)
        cv2.putText(image, f"{ranking}", (x-5, y+5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(image, f"{team}: {value:.2f}", (x-50, 50+(i%2)*25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        
        string = f"^ {spring} v" if spring > 0 else f"v {abs(spring)} ^"
        if spring == 0: string = f"= {spring} ="

        # cv2.rectangle(image, (x + XSTEP//2 - 30, (y + y2)//2 - 15), (x + XSTEP//2 + 30, (y + y2)//2 + 10), (0, 0, 0), -1)
        cv2.putText(image, string, (x + XSTEP//2 - 20, (y + y2)//2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    show(image, timeout)

def solve_spring_system(current:list[float], springs:list[float], step:float=0.01) -> list[float]:
    step = float(step) # Convert from np.float to python float
    n = len(current)
    new = current.copy()
    print(f"[solve] Step: {step:.4f}")
    # Logging
    print("[solve] Springs: ", " | ".join([ f"{_:>5.1f}" for _ in springs ]))
    print("[solve] Current: ", " | ".join([ f"{_:>5.1f}" for _ in current ]))

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

        print(f"[solve]    At team {TEAMS_CYCLE[i]:<16} | sl {spring_left:>5.1f} | sr {spring_right:>5.1f} | dl {diff_left:>5.1f} | dr {diff_right:>5.1f} | ml {move_left:>5.1f} | mr {move_right:>5.1f}") 

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
    render(TEAMS_CYCLE, springs, current, timeout=0)

    for i in range(1000):
        print(f"Step {i:>5} ", end="\r")
        render(TEAMS_CYCLE, springs, current, timeout=33)
    
        current = solve_spring_system(current, springs, step=0.01 + 0.01*i)
    
        if np.allclose(current, prev, atol=0.0001):
            print(f"Scores converged at step {i}")
            break
    
        prev = current
    
    score_team = list(zip(current, TEAMS_CYCLE))
    for score, team in sorted(score_team, reverse=True):
        print(f"{team:<16} | {score:.2f}")

    # System converged. Render the final state
    render(TEAMS_CYCLE, springs, current, timeout=0)
