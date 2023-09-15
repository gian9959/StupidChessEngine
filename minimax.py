import chess


def minimax(state, depth, alpha, beta, is_maximizing_player):
    state.counter = state.counter + 1

    if depth == 0 or state.is_game_over():
        return state.evaluate()

    if is_maximizing_player:
        best_score = -float('inf')
        moves = state.get_ordered_moves()
        for move in moves:
            state.board.push(move)
            score = minimax(state, depth - 1, alpha, beta, False)
            state.board.pop()
            best_score = max(best_score, score)
            if best_score >= beta:
                break
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        moves = state.get_ordered_moves()
        for move in moves:
            state.board.push(move)
            score = minimax(state, depth - 1, alpha, beta, True)
            state.board.pop()
            best_score = min(best_score, score)
            if best_score <= alpha:
                break
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score
