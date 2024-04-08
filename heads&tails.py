import random

HEADS = "Орёл"
TAILS = "Решка"
COIN_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES)


print(flip_coin())
