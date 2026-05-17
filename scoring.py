POINTS_CORRECT = 10
POINTS_WRONG = 0  # oppure -5, documenta la scelta nel README

def apply_answer(score: int, is_correct: bool) -> int:
    if is_correct:
        return score + POINTS_CORRECT
    return score + POINTS_WRONG