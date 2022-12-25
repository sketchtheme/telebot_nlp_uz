import re

from typing import List


def token_to_syllables(token: str) -> List[str]:

    if len(token) < 2:
        return [token]
    # if (token == 'aaa', 'oie', 'iao','oooaoa','ieieieie',"o'oao","ao'"):
    #     return "Iltimos to'g'ri so'z kiriting"

    VOWELS = "aoieuo"
    UNPAIRED_SONANTS = "rlmnpqbdfghjkltvxy"
    SIGNS = "'"

    break_indices = [i + 1 for i, letter in enumerate(token) if letter in VOWELS]
    if len(break_indices) < 2:
        return [token]

    for i, indice in enumerate(break_indices[:-1]):
        letter = token[indice]
        next_letter = token[indice + 1 : indice + 2]
        # Slice is used to defeat IndexError on last letter

        if (
            letter in UNPAIRED_SONANTS
            and next_letter not in VOWELS
            and letter != next_letter
            and not (letter in "rR" and next_letter in "jJ")
            and next_letter not in SIGNS
        ):
            break_indices[i] += 1
        elif letter in UNPAIRED_SONANTS and next_letter in SIGNS:
            break_indices[i] += 2
        elif letter in "yY" and next_letter not in VOWELS:
            break_indices[i] += 1



    break_indices.insert(0, 0)
    del break_indices[-1]

    return [token[i:j] for i, j in zip(break_indices, break_indices[1:] + [None])]


def word_to_syllables(word: str) -> List[str]:

    syllables = []

    for subword in word.split("-"):
        if subword:
            syllables += token_to_syllables(subword)

    if not syllables: syllables = [""]
    return syllables


# def word_to_syllables_wd(word: str) -> List[str]:
#
#     syllables = []
#
#     for subword in word.split("-"):
#         if subword:
#             syllables += token_to_syllables(subword) + ["-"]
#         else:
#             syllables.append("-")
#
#     return syllables[:-1]


def word_to_syllables_safe(word: str) -> List[str]:

    assert bool(
        re.match(r"\A[a-А-ouie-]*\Z", word)
    ), "Word contains unsuitable symbols"

    return word_to_syllables(word)


# def word_to_syllables_safe_wd(word: str) -> List[str]:
#
#     assert bool(
#         re.match(r"\A[a-А-ouie-]*\Z", word)
#     ), "Word contains unsuitable symbols"
#     assert bool(
#         re.match(r"\A[a-А-ouie-]*\Z", word)
#     ), "Word contains unsuitable symbols"
#
#     return word_to_syllables_wd(word)


def main() -> None:

    word = input("Word: ").lower()
    return word_to_syllables_safe(word)


while True:
    print(main())
