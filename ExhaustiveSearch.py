#Depth-First Search
def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_dfs(N, row=0, board=None, solutions=None):
    if board is None:
        board = [-1] * N
    if solutions is None:
        solutions = []
    
    if row == N:
        solutions.append(board[:])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens_dfs(N, row + 1, board, solutions)
            board[row] = -1  # Backtrack
    
    return solutions

# Test for N=10
import time
N = 10
start_time = time.time()
solutions = solve_n_queens_dfs(N)
end_time = time.time()

print(f"Number of solutions for N={N}: {len(solutions)}")
print(f"Time taken: {end_time - start_time:.2f} seconds")