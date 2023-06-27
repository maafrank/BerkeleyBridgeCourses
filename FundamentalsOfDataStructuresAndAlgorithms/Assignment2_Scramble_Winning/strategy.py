 
"""
For this problem, let’s consider a two-player version of the decreasing
number game. The game begins with a number N - this is the state of the
game. Two players take turns decreasing the number. Each player has
two moves available: they can subtract 1 from the number, or divide it in
half (not integer division - use floats for this!). The player that decreases 
the number below 1 is the loser.
"""


def is_hot(num):
    if num < 2:
        return False
