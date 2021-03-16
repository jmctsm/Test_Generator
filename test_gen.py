#!python

"""
Generates a matching file 
"""

import random
import string
from typing import KeysView


def random_letter():
    if len(key_words) > 26:
        return f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}"
    else:
        return random.choice(string.ascii_uppercase)


if __name__ == "__main__":
    key_words = [
        "electromagnetic spectrum",
        "laser",
        "cornea",
        "eyebrow",
        "eyelash",
        "eyelid",
        "iris",
        "lens (eye)",
        "optic nerve",
        "pupil",
        "retina",
        "tear",
        "vitreous",
        "hologram",
        "Common characteristic of all optical devices",
        "refracting telescope",
        "reflecting telescope",
        "microscope",
        "rods and cones",
        "rod",
        "cone",
        "lens",
        "concave",
        "convex",
    ]
    definitions = [
        "range of wavelengths or frequencies over which electromagnetic radiation extends",
        "light amplification through stimulated emissions of radiation",
        "the clear, dome-shaped tissues covering the front of the eye",
        "a patch of dense hairs located above the eye",
        "one of the many hairs on the edge of the eyelids",
        "the flap of skin that can cover and protect the eye",
        "the colored part of the eye; it controls the amount of light that enters the eye by changing the size of the pupil",
        "a crystalline structure located just behind the iris; it focuses light onto the retina",
        "the nerve that transmits electrical impulses from the retina to the brain",
        "the opening in the center of the iris; it changes size as the amount of light changes; the more light, the smaller the hole",
        "sensory tissue that lines the back of the eye; it contains millions of photoreceptors (rods and cones) that convert light rays into electrical impulses that are relayed to the brain via the optic nerve",
        "clear, salty liquid that is produced by glands in the eyes",
        "a thick, transparent liquid that fills the center of the eye; it is mostly water and gives the eye its form and shape; also called the vitreous humor",
        "three-dimensional photograph that is produced using lasers",
        "all produce or control light",
        "uses lenses to gather and focus light from distant objects",
        "uses mirrors to gather and focus light from distant objects",
        "uses lenses to form a magnified image of very small, close objects",
        "cells in the retina",
        "responds to low light",
        "responds to wavelength of colors",
        "transparent object with at least one curved side that causes light to change",
        "thicker at the edges than in the middle",
        "thicker in the middle than at the edge",
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
    for key in key_words:
        print(f"{counter + 1}.  _____{key_words[counter]}")
        counter += 1
    print("\n\n\n")
    for key in test_dict.keys():
        print(f"{key}.  {test_dict[key]}")
    print("\n\n\nANSWERS")
    for x in range(len(answer_list)):
        print(f"{x + 1} {key_words[x]} : {answer_list[x]}")
