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
        "absorption behavior of light waves",
        "concave mirror",
        "convex mirror",
        "diffuse reflection",
        "Electro magnetic radiation",
        "focal length",
        "focal point",
        "illuminated",
        "image",
        "law of reflection",
        "lens",
        "light",
        "luminous",
        "mirror that curves inward like the bowl of a spoon",
        "moon, trees, people",
        "opaque materials",
        "optical axis	",
        "parallel",
        "plane mirror",
        "reflection",
        "regular reflection",
        "scattered",
        "sun, traffic light, firefly",
        "translucent and opaque",
        "translucent materials",
        "transmission behavior of light waves",
        "transparent materials",
        "transparent, translucent",
        "transparent, translucent, opaque",
    ]
    definitions = [
        "transfer of energy by a wave to the medium through which it passes",
        "produces a real image beyond that focal point, no image at the focal point, and a virtual image if viewed closer than the focal point",
        "produces a virtual image that appears smaller than the actual object",
        "reflection of light from a rough surface",
        "energy carried through space or matter by electromagnetic wave",
        "the distance along the optical axis from the mirror to the focal point",
        "the point where light rays parallel to the optical axis converge after being reflected by a mirror or refracted by a lens",
        "objects that reflect light but don't produce it",
        "figure, pattern, or reflection of an object",
        "the angle of incidence is equal to the angle of reflection",
        "a transparent object with at least one curved side that causes light to change direction",
        "electromagnetic reflects that you can see",
        "object that produces and emits their own light",
        "concave mirror",
        "examples of illuminated",
        "light does not pass through",
        "Line perpendicular to the center of the mirror",
        "reflected rays of regular reflection",
        "produces a virtual image that appears to be behind the surface of the mirror",
        "the bouncing of a wave off a surface",
        "reflection of light from a smooth, shiny surface",
        "reflected rays of diffuse reflection",
        "examples of luminous",
        "types of reflection of materials",
        "allows most of the light that strikes it to pass through and form a blurry image",
        "passage of light through an object",
        "allows most all the light that strikes it to pass through and form a clear image",
        "types of transmission of materials",
        "types of absorbing of materials",
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
