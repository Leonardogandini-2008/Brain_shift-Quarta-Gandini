import random
import string
from models import Trial
from rules import compute_expected_answer

def generate_trial(rng: random.Random) -> Trial:
    position = rng.choice(["TOP", "BOTTOM"])
    letter = rng.choice(list(string.ascii_uppercase))
    number = rng.randint(1, 9)
    expected = compute_expected_answer(position, letter, number)
    return Trial(
        position=position,
        letter=letter,
        number=number,
        expected_answer=expected
    )