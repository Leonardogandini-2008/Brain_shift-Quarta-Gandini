from dataclasses import dataclass

@dataclass
class Trial:
    position: str          # "TOP" o "BOTTOM"
    letter: str            # lettera maiuscola A-Z
    number: int            # intero 1-9
    expected_answer: bool  # calcolata da compute_expected_answer
    user_answer: bool | None = None
    is_correct: bool = False