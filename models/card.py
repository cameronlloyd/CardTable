from enums import Rank, Suit


class Card:
    """
    A class to represent a playing card

    Attributes
    ----------
    rank: Rank
        The rank of the playing card (e.g. 2, 3, K, A, etc.)
    suit: Suit
        The suit of the playing card (e.g. Clubs, Spades, etc.)
    face_up: bool
        Whether the playing card should be face up without it's value hidden or not
    """

    def __init__(self, rank: Rank, suit: Suit, face_up: bool = False):
        if not isinstance(rank, Rank):
            raise Exception(f'{rank} is not a valid rank')
        if not isinstance(suit, Suit):
            raise Exception(f'{suit} is not a valid suit')

        self.rank = rank
        self.suit = suit
        self.face_up = face_up

    def flip(self) -> None:
        """Toggle whether the card is face up or down"""
        self.face_up = not self.face_up

    def __str__(self):
        """Draw the given playing card.  Card will be hidden if the card is face down"""
        card = "┌───────┐\n"

        # Disguise face value if card isn't flipped
        if self.face_up:
            card += f"| {self.rank.value:<2}    |\n"
            card += "|       |\n"
            card += f"|   {self.suit.value}   |\n"
            card += "|       |\n"
            card += f"|    {self.rank.value:>2} |\n"
        else:
            card += "| ----- |\n"
            card += "| ----- |\n"
            card += "| ----- |\n"
            card += "| ----- |\n"
            card += "| ----- |\n"

        card += "└───────┘"
        return card
