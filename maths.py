import numpy as np


def step_solution(current:list[float], forces:list[float], step:float=0.01) -> list[float]:
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

def is_single_cycle(teams, matches):
    """
    Check if the matches form a single cycle where each team plays against exactly two other teams.
    
    Args:
        teams: List of team names
        matches: List of matches, where each match is [team1, team2, score1, score2]
        
    Returns:
        bool: True if matches form a single cycle, False otherwise
    """
    # Create a graph representation where each team is connected to the teams it played against
    graph = {team: [] for team in teams}
    
    # Build the graph from matches
    for match in matches:
        team1, team2 = match[0], match[1]
        graph[team1].append(team2)
        graph[team2].append(team1)
    
    # Check if each team has exactly 2 connections (one to each side in the cycle)
    for team, connections in graph.items():
        if len(connections) != 2:
            return False
    
    # Check if the graph is connected (all teams are reachable from the first team)
    visited = set()
    
    def dfs(team):
        visited.add(team)
        for neighbor in graph[team]:
            if neighbor not in visited:
                dfs(neighbor)
    
    # Start DFS from the first team
    dfs(teams[0])
    
    # If all teams were visited, it's a single cycle
    return len(visited) == len(teams)
