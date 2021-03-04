#!python

"""
Generates a matching file 
"""

import random
import string
from typing import KeysView


def random_letter():
    return random.choice(string.ascii_uppercase)


if __name__ == "__main__":
    key_words = [
        "Tone Quality",
        "Characteristic Sound (timbre)",
        "Dynamics",
        "Intonation (some judges call this 'Pitch')",
        "Balance (blend)",
        "Precision",
        "Interpretation",
        "Articulation",
        "Technique",
        "Ensemble sound",
    ]
    definitions = [
        "Beauty of Sound",
        "the intended sound an instrument should make",
        "volume (loudness or softness) of music (and all shadings between)",
        "being in tune with other instruments (two or more sounding as one)",
        "Each instrument being equally heard",
        "Playing at the exactly the same time",
        "tempo, dynamics, articulations, etc. that the composer intended",
        "the style notes begin and end (tonguing style)",
        "fluency of articulation and fingering",
        "Each member blending with the rest of the band (combining Tone Quality, Intonation, Balance, and Precision)",
    ]
    test_dict = {}
    answer_list = {}
    counter = 0
    used_numbers = []
    while True:
        if len(test_dict) > len(key_words):
            break
        letter = random_letter()
        if letter in test_dict.keys():
            continue
        random_number = random.randint(0, len(key_words) - 1)
        if random_number in used_numbers:
            continue
        used_numbers.append(random_number)
        test_dict[letter] = definitions[random_number]
        answer_list[random_number] = letter
        if len(test_dict) == len(key_words):
            break
        counter += 1
    print("QUIZ")
    counter = 0
    for key in test_dict.keys():
        print(
            f"{counter + 1}.  _____{key_words[counter]}                     {key}.  {test_dict[key]}"
        )
        counter += 1
    print("\n\n\nANSWERS")
    for x in range(len(answer_list)):
        print(f"{x + 1} {key_words[x]} : {answer_list[x]}")
