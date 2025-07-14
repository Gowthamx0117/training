def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
            # Check diagonals
            if abs(board[i] - col) == row - i:
                return False
        return True

    def solve(row, board, solutions):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1, board, solutions)
                board[row] = -1

    solutions = []
    solve(0, [-1]*n, solutions)
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for i in range(n):
            row = ['.']*n
            row[sol[i]] = 'Q'
            print(' '.join(row))
        print()

if __name__ == "__main__":
    n = int(input("Enter number of Queens: "))
    solutions = solve_n_queens(n)
    print(f"Total solutions for {n}--Queens: {len(solutions)}\n")
    print_solutions(solutions, n)