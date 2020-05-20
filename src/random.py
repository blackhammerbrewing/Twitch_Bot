from random import randint


def roll_int(ctx):
    """
    User input determines the upper bound on the random int.
    Returns an integer between 1 and rollNum.
    """
    rollNum = ctx.content.split(' ')
    if len(rollNum) > 1 and rollNum[1].isnumeric() is True:
        return randint(1, int(rollNum[1]))
    else:
        return None
