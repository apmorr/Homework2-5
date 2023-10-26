def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""

    if not p_idxs:  # base case - puzzle is not solved
        return True
    moves = valid_moves(k_idx)  # Finds all valid moves
    for move in moves:
        if move in p_idxs:  # trys all valid moves
            new_pawns = p_idxs - {move}
            if solveable(new_pawns, move):
                return True
    return False  # if all failed returns false


def valid_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    row, col = k_idx
    possible_moves = {(row - 1, col - 2), (row - 2, col - 1), (row - 2, col + 1), (row - 1, col + 2),
                      (row + 1, col - 2), (row + 2, col - 1), (row + 2, col + 1), (row + 1, col + 2)}
    # creates a list of all possible moves at the given point

    return set(filter(lambda x: 0 <= x[0] <= 7 and 0 <= x[1] <= 7, possible_moves))
    # compares each item in the list, only returns the moves inside the 8x8 chessboard
