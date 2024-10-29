
def is_safe(board, row, col):
    # Kontrollo rreshtin dhe kolonën
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Kontrollo diagonalen e sipërme të majtë
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Kontrollo diagonalen e poshtme të majtë
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_dls(board, col, limit):
    # Nëse kemi vendosur të gjitha mbretëreshat, kthe True
    if col >= len(board):
        return True

    if limit == 0:
        return False
    # Provo të vendosësh mbretëreshën në secilin rresht
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Vendos mbretëreshën në pozicionin [i][col]
            board[i][col] = 1
            # Provo të vendosësh mbretëreshën e radhës (me limit të reduktuar
            if solve_n_queens_dls(board, col + 1, limit - 1):
                return True
            # Nëse nuk funksionon, hiq mbretëreshën (backtrack)
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print("\n")

def main():
    N = 8  # Dimensioni i tabelës (8x8 për problemin e mbretëreshave)
    limit = 8  # Kufiri i thellësisë për DLS
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solve_n_queens_dls(board, 0, limit):
        print("Zgjidhja e problemit të tetë mbretëreshave:")
        print_board(board)
    else:
        print("Nuk u gjet asnjë zgjidhje.")

if __name__ == "__main__":
    main()
