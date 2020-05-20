def voting(winners, author, text):
    if author not in winners.keys():
        if text.isnumeric():
            winners[author] = text
    return winners
