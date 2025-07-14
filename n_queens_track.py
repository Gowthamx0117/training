def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                print(f"  ❌ Not safe to place at ({row},{col}) due to conflict with ({i},{board[i]})")
                return False
        print(f"  ✅ Safe to place at ({row},{col})")
        return True

    def solve(row, board, solutions):
        if row == n:
            print(f"\n🎯 Solution found: {board}")
            solutions.append(board[:])
            return
        print(f"\n🔽 Trying to place queen in row {row}")
        for col in range(n):
            print(f"🔍 Checking position ({row}, {col})")
            if is_safe(board, row, col):
                board[row] = col
                print(f"➡️  Placed queen at ({row}, {col}) → {board}")
                solve(row + 1, board, solutions)
                print(f"↩️  Backtracking from ({row}, {col})")
                board[row] = -1

    solutions = []
    solve(0, [-1] * n, solutions)
    return solutions

def print_solutions(solutions, n):
    print(f"\n🧮 Total solutions: {len(solutions)}\n")
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for i in range(n):
            row = ['.'] * n
            row[sol[i]] = 'Q'
            print(' '.join(row))
        print()

if __name__ == "__main__":
    n = int(input("Enter number of Queens: "))
    solutions = solve_n_queens(n)
    print_solutions(solutions, n)
