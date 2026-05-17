VOWELS = set("AEIOU")

def is_even(number: int) -> bool:
    return number % 2 == 0

def is_vowel(letter: str) -> bool:
    return letter.upper() in VOWELS

def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    if position == "TOP":
        return is_even(number)
    elif position == "BOTTOM":
        return is_vowel(letter)
    else:
        raise ValueError(f"Posizione non valida: {position}")