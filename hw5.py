def valid_moves(k_idx):
    row, col = k_idx
    possible_moves = {(row - 1, col - 2), (row - 2, col - 1), (row - 2, col + 1), (row - 1, col + 2),
                      (row + 1, col - 2), (row + 2, col - 1), (row + 2, col + 1), (row + 1, col + 2)}
    return set(filter(lambda x: 0 <= x[0] <= 7 and 0 <= x[1] <= 7, possible_moves))


def solveable(p_idxs, k_idx):
    if not p_idxs:  # base case, no pawns left to capture
        return True
    moves = valid_moves(k_idx)
    for move in moves:
        if move in p_idxs:  # capture pawn and move knight
            new_pawns = p_idxs - {move}
            if solveable(new_pawns, move):
                return True
    return False
