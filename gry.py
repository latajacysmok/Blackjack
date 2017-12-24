class Player(object):
    """ Uczestnik gry. """
    def __init__(self):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """ Zadaj pytanie, na które można odpowiedzieć tak lub nie"""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Poproś o podanie liczby z określonego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response