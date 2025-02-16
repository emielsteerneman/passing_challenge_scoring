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
TEAMS_CYCLE = [ERFORCE, TIGERS, KIKS, ROBODRAGONS, ZJUNLICT]

MATCHES = [
    [ZJUNLICT, ERFORCE, 5, 2],
    [ERFORCE, TIGERS, 4, 1],
    [TIGERS, KIKS, 45, 3],
    [KIKS, ROBODRAGONS, 8, 11],
    [ROBODRAGONS, ZJUNLICT, 12, 50]
]

# ZJUNLict    - 55 passes total
# ER-Force    -  6 passes total
# TIGERS     - 46 passes total
# KIKS        - 11 passes total
# RoboDragons - 23 passes total

## Ranking based on passes:
# ZJUNLict > TIGERS > RoboDragons > KIKS > ER-Force
# This makes no sense since ER-Force won against TIGERS and basically tied with ZJUNLict





# """ 2024 TOURNAMENT """
# TEAMS_CYCLE = [ERFORCE, LUHBOTS, KIKS, RTT, TIGERS, ROBODRAGONS, ZJUNLICT]

# # Match schedule here https://docs.google.com/spreadsheets/d/1wFbCYw-gfPdE7WykX31WSTPAvU3SWHysxapoCXWekbA/edit?gid=1087321196#gid=1087321196
# # Score sheet    here https://docs.google.com/spreadsheets/d/1KiqHZhVfNrZQpCc0nftIHPvuw9C-P_diZZ-TQojkGdM/edit?gid=1863286970#gid=1863286970
# MATCHES = [
#     [ERFORCE, LUHBOTS, 9, 4],
#     [ZJUNLICT, ROBODRAGONS, 67, 0],
#     [RTT, TIGERS, 5, 52],
#     [KIKS, RTT, 5, 17],
#     [TIGERS, ROBODRAGONS, 65, 1],
#     [ERFORCE, ZJUNLICT, 5, 11],
#     [KIKS, LUHBOTS, 7, 10]
# ]

# ER-Force 9 - 4 LUHBots 10 - 7 KIKS 5 - 17 RTT 5 - 52 TIGERs Mannheim 65 - 1 RoboDragons 0 - 67 ZJUNlict 11 - 5 ER-Force

# TEAM            - TOTAL PASSES        ORIGINAL RANK       RANK WITH THIS SYSTEM       RESULT
# ER-Force        - 14 passes total     4th place shared    3rd place                   Moved up
# LUHBots         - 14 passes total     4th place shared    4th place
# KIKS            - 12 passes total     6th place           6th place
# RoboTeam Twente - 22 passes total     3rd place           5th place                   Dropped down
# TIGERs Mannheim - 117 passes total    1st place           1st place
# RoboDragons     - 1 pass total        7th place           7th place
# ZJUNlict        - 78 passes total     2nd place           2nd place



def show(image, timeout=0):
    cv2.imshow("image", image)
    if cv2.waitKey(timeout) == ord('q'):
        exit()

def render(teams, springs, values, timeout=0):
    GRID_STEP = 4
    WHITE = (255, 255, 255)
    BACKGROUND = (10, 10, 10)
    FONT = cv2.FONT_HERSHEY_SIMPLEX

    image = np.zeros((800, 1200, 3), np.uint8)
    image.fill(BACKGROUND[0])
    YCENTER = int(image.shape[0] * 0.8)
    XSTEP = 1000 // len(teams)

    # Determine minimum and maximum values. Check if frame needs to be resized
    upper_y, lower_y = YCENTER - max(values)*GRID_STEP, YCENTER - min(values)*GRID_STEP
    if upper_y < 0 or 1200 < lower_y:
        print("NOT GOING TO FIT!")
        # Modify grid step to fit the values
        GRID_STEP = min(6, 0.8*(YCENTER)/max(values), 0.8*(1200-YCENTER)/min(values))
    print("Upper Y:", upper_y, "Lower Y:", lower_y, "Grid step:", GRID_STEP)

    to_x = lambda x: 200 + int(x*XSTEP)
    to_y = lambda y: YCENTER - int(y*GRID_STEP)


    ### Draw grid
    for i in range(0, 140, 10):
        # Vertical
        # cv2.line(image, (20*i, 0), (20*i, 1000), (20, 20, 20), 1)
        # Horizontal
        cv2.line(image, (0, to_y(i)), (1200, to_y(i)), (50, 50, 50), 1)
        cv2.line(image, (0, to_y(-i)), (1200, to_y(-i)), (50, 50, 50), 1)
    cv2.line(image, (0, to_y(0)), (1200, to_y(0)), WHITE, 1)

    ### Draw teams
    get_color = lambda i: (255 - i*50, 0, i*50)

    values_shift_one = values[1:] + [values[0]]
    for i, (team, spring, value, next_value) in enumerate(zip(teams, springs, values, values_shift_one)):
        x, y = to_x(i), to_y(value)# YCENTER-int(value*GRID_STEP)
        x2, y2 = to_x(i+1), to_y(next_value) #YCENTER-int(values[(i+1)%len(teams)]*GRID_STEP)

        # Determine ranking of team
        ranking = sum([ v >= value for v in values ])
        # Draw circle, ranking within the circle, and name at the top
        cv2.circle(image, (x, y), 20, get_color(i), -1, cv2.LINE_AA)
        cv2.putText(image, f"{ranking}", (x-5, y+5), FONT, 0.5, WHITE, 1, cv2.LINE_AA)
        cv2.putText(image, f"{team}: {value:.2f}", (x-50, 50+(i%2)*25), FONT, 0.5, WHITE, 1, cv2.LINE_AA)

        
        string = f"^ {spring} v" if spring > 0 else f"v {abs(spring)} ^"
        if spring == 0: string = f"= {spring} ="

        # Draw a fancy spring (zigzagging lines)
        spring_x = x + XSTEP//2
        dy = abs(y - y2)
        spring_ = abs(spring)
        for i in range(spring_):
            wire_x1 = 5 if i % 2 == 0 else -5
            wire_y1 = min(y, y2) + int(i * (dy/spring_))
            wire_x2 = 5 if i % 2 == 1 else -5
            wire_y2 = min(y, y2) + int((i+1) * (dy/spring_))
            cv2.line(image, (spring_x + wire_x1, wire_y1), (spring_x + wire_x2, wire_y2), (255, 255, 0), 1, cv2.LINE_AA)

        cv2.putText(image, string, (x + XSTEP//2 - 20, (y + y2)//2), FONT, 0.6, BACKGROUND, 4, cv2.LINE_AA)
        cv2.putText(image, string, (x + XSTEP//2 - 20, (y + y2)//2), FONT, 0.6, WHITE, 1, cv2.LINE_AA)

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
    # initial = [ 0. for team in TEAMS_CYCLE ]
    initial = [ passes_per_team[team] for team in TEAMS_CYCLE ]
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
        render(TEAMS_CYCLE, springs, current, timeout=200)
    
        current = solve_spring_system(current, springs, step=0.01 + 0.01*i)
    
        if np.allclose(current, prev, atol=0.0001):
            print(f"Scores converged at step {i}")
            break
    
        prev = current
    
    score_team = list(zip(current, TEAMS_CYCLE))
    for score, team in sorted(score_team, reverse=True):
        print(f"{team:<16} | {score:.2f}")

    # System converged. Render the final state
    render(TEAMS_CYCLE, springs, current, 0)
