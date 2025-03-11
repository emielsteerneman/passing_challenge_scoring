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





def solve_force_system(current:list[float], forces:list[float], step:float=0.01) -> list[float]:
    step = float(step) # Convert from np.float to python float
    n = len(current)
    new = current.copy()

    # For each team
    for i in range(n):
        i_left, i_right = (i-1+n)%n, (i+1)%n
        # Get the force force between the current team and the team to the left and right
        force_left, force_right = -forces[i_left], forces[i]
        # Calculate the difference between the current state and the force force
        diff_left, diff_right = (current[i] - current[i_left]), (current[i] - current[i_right])
        # Calculate the movement of the team based on the difference
        move_left, move_right = (force_left - diff_left), (force_right - diff_right)
        # Step the team based on the movement
        step_size = step * (move_left + move_right)
        new[i] += step_size

    return new

def closed_form_solution(forces: list[float]) -> list[float]:
    """
    Computes a closed-form solution for the team scores based on input forces (differences in passing scores).
    
    The method constructs a reduced Laplacian matrix by fixing the score of the first team (x[0] = 0) 
    to remove the degree of freedom caused by the invariance to an additive constant. 
    For teams 1..n-1, the system is described by:
        -2*x[i] + x[i-1] + x[i+1] = forces[i-1] - forces[i]
    
    This gives L*x=b, where L is the Laplacian matrix
    
    After solving the system, the full score vector is reconstructed by prepending the fixed value x[0] = 0.
    
    Returns:
        A list of team scores (floats) normalized relative to the first team.
    """
    n = len(forces)
    # Initialize the reduced Laplacian matrix L and right-hand side vector b.
    L = np.zeros((n - 1, n - 1))
    b = np.zeros(n - 1)
    
    # Build L and b for teams 1 through n-1.
    for i in range(1, n):
        row = i - 1  # Map team index to row index in L and b.
        # Diagonal element for team i: corresponds to -2 * x[i]
        L[row, row] = -2
        
        # Neighbor to the left (if exists)
        if i - 2 >= 0:
            L[row, row - 1] = 1
        
        # Neighbor to the right (if exists)
        if i < n - 1:
            L[row, row + 1] = 1
        
        # The right-hand side is defined by the difference in forces between the left neighbor and the current team.
        b[row] = forces[i - 1] - forces[i]
    
    # Solve the linear system for the unknown scores (excluding the first fixed score).
    x_unknown = np.linalg.solve(L, b)
    
    # Reconstruct full score vector with x[0] fixed at zero.
    x = np.zeros(n)
    x[1:] = x_unknown
    return x.tolist()

def normalize_scores(scores: list[float]) -> list[float]:
    # Normalize scores by subtracting the minimum score
    m = min(scores)
    return [s - m for s in scores]

def print_scores(header: str, scores: list[float], teams: list[str]) -> None:
    print(header)
    for score, team in sorted(zip(scores, teams), reverse=True):
        print(f"{team:<16} | {score:.2f}")

if __name__ == "__main__":

    get_total_passes = lambda matches, team: sum([ m[m.index(team)+2] for m in matches if team in m ])

    # Calculate total passes per team
    passes_per_team = { team: get_total_passes(MATCHES, team) for team in TEAMS_CYCLE }

    # Create initial state
    initial = [ 0. for team in TEAMS_CYCLE ]
    forces = []
    # For each team pair that played against each other, calculate the difference in passes
    for team1, team2 in zip(TEAMS_CYCLE, TEAMS_CYCLE[1:] + [TEAMS_CYCLE[0]]):
        # Find the match between the two teams
        match = [ m for m in MATCHES if team1 in m and team2 in m ][0]
        # Get the total passes for each team
        s1, s2 = match[match.index(team1)+2], match[match.index(team2)+2]
        # The difference in passes is the force value. See drawing.drawio for more info
        forces.append(s1-s2)

    # Iteratively solve the force system until it converges
    current = initial
    prev = [0.0] * len(TEAMS_CYCLE)

    for i in range(1000):
    
        current = solve_force_system(current, forces, step=0.01 + 0.01*i)
    
        if np.allclose(current, prev, atol=0.0001):
            print(f"Scores converged at step {i}")
            break
    
        prev = current
    
    normalized_current = normalize_scores(current)
    print_scores("Final scores:", normalized_current, TEAMS_CYCLE)

    cf_solution = closed_form_solution(forces)
    normalized_cf = normalize_scores(cf_solution)
    print_scores("Closed form solution:", normalized_cf, TEAMS_CYCLE)