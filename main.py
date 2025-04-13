import cv2
import numpy as np
from maths import step_solution, closed_form_solution, is_single_cycle, normalize_scores
from matches import Team, load_2024_tournament

def show(image, timeout=0):
    cv2.imshow("image", image)
    if cv2.waitKey(timeout) == ord('q'):
        exit()

def render(teams, forces, values, timeout=0):
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
    # print("Upper Y:", upper_y, "Lower Y:", lower_y, "Grid step:", GRID_STEP)

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
    for i, (team, force, value, next_value) in enumerate(zip(teams, forces, values, values_shift_one)):
        x, y = to_x(i), to_y(value)# YCENTER-int(value*GRID_STEP)
        x2, y2 = to_x(i+1), to_y(next_value) #YCENTER-int(values[(i+1)%len(teams)]*GRID_STEP)

        # Determine ranking of team
        ranking = sum([ v >= value for v in values ])
        # Draw circle, ranking within the circle, and name at the top
        cv2.circle(image, (x, y), 20, get_color(i), -1, cv2.LINE_AA)
        cv2.putText(image, f"{ranking}", (x-5, y+5), FONT, 0.5, WHITE, 1, cv2.LINE_AA)
        cv2.putText(image, f"{team}: {value:.2f}", (x-50, 50+(i%2)*25), FONT, 0.5, WHITE, 1, cv2.LINE_AA)

        
        string = f"^ {force} v" if force > 0 else f"v {abs(force)} ^"
        if force == 0: string = f"= {force} ="

        # Draw a fancy force (zigzagging lines)
        force_x = x + XSTEP//2
        dy = abs(y - y2)
        force_ = abs(force)
        for i in range(force_):
            wire_x1 = 5 if i % 2 == 0 else -5
            wire_y1 = min(y, y2) + int(i * (dy/force_))
            wire_x2 = 5 if i % 2 == 1 else -5
            wire_y2 = min(y, y2) + int((i+1) * (dy/force_))
            cv2.line(image, (force_x + wire_x1, wire_y1), (force_x + wire_x2, wire_y2), (255, 255, 0), 1, cv2.LINE_AA)

        cv2.putText(image, string, (x + XSTEP//2 - 20, (y + y2)//2), FONT, 0.6, BACKGROUND, 4, cv2.LINE_AA)
        cv2.putText(image, string, (x + XSTEP//2 - 20, (y + y2)//2), FONT, 0.6, WHITE, 1, cv2.LINE_AA)

    show(image, timeout)

def calculate_forces(teams, matches):
    get_total_passes = lambda matches, team: sum([ m[m.index(team)+2] for m in matches if team in m ])

    # Calculate total passes per team
    passes_per_team = { team: get_total_passes(matches, team) for team in teams }

    initial = [ passes_per_team[team] for team in teams ]
    forces = []
    
    for team1, team2 in zip(teams, teams[1:] + [teams[0]]):
        match = [ m for m in matches if team1 in m and team2 in m ][0]
        s1, s2 = match[match.index(team1)+2], match[match.index(team2)+2]
        forces.append(s1-s2)
    
    return initial, forces

def run_step_system(initial, forces):
    # Iteratively solve the force system until it converges
    current = initial
    prev = [0.0] * len(TEAMS_CYCLE)
    render(TEAMS_CYCLE, forces, current, timeout=0)

    for i in range(1000):
        # print(f"Step {i:>5} ", end="\r")
        render(TEAMS_CYCLE, forces, current, timeout=50)
    
        current = step_solution(current, forces, step=0.01 + 0.01*i)
    
        if np.allclose(current, prev, atol=0.0001):
            # print(f"Scores converged at step {i}")
            break
    
        prev = current

    return current

if __name__ == "__main__":

    TEAMS_CYCLE, MATCHES = load_2024_tournament()

    # Check if MATCHES forms a single cycle
    if not is_single_cycle(TEAMS_CYCLE, MATCHES):
        raise ValueError("Matches do not form a single cycle. The scoring system may not work correctly.")
    
    initial, forces = calculate_forces(TEAMS_CYCLE, MATCHES)

    closed_form_answer = closed_form_solution(forces)
    closed_form_answer = normalize_scores(closed_form_answer)
    score_team = list(zip(closed_form_answer, TEAMS_CYCLE))
    print(f"Closed form answer:")
    for score, team in sorted(score_team, reverse=True):
        print(f"{team:<16} | {score:.2f}")

    print("Step system answer:")
    step_answer = run_step_system(initial, forces)
    step_answer = normalize_scores(step_answer)
    score_team = list(zip(step_answer, TEAMS_CYCLE))
    for score, team in sorted(score_team, reverse=True):
        print(f"{team:<16} | {score:.2f}")
    
