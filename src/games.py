def voting(winners, author, text):
    """
    Every author gets to vote once with their vote being text. The text is a
    numberic string indicating a voting choice. Each vote is added to a dict of
    all other votes.
    """
    if author not in winners.keys():
        if text.isnumeric():
            winners[author] = text
    return winners
