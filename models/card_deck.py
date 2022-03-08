from __future__ import annotations      # Allow typing hinting a method with the type of the enclosing class (i.e. CardDeck).
                                        # Support for this may be included in a future release of python

from .card import Card
from enums import Rank, Suit
from typing import List
import random


class CardDeck:
    """
    A class to represent a deck of playing cards (excluding Jokers)

    Attributes
    ----------
    cards: List[Card]
        The cards in the deck
    """

    def __init__(self, cards: List[Card]=None):
        if not cards:
            # Build complete deck of 52 cards (excluding Jokers)
            self.cards = [Card(rank, suit) for rank in Rank for suit in Suit]
            self.shuffle()
        else:
            self.cards = cards

    def shuffle(self) -> None:
        """Shuffle the deck and set all cards face down"""
        random.shuffle(self.cards)
        for card in self.cards:
            card.face_up = False

    def card_count(self) -> int:
        """Count the number of cards in the deck"""
        return len(self.cards)

    def deal(self, number_of_hands: int) -> List[CardDeck]:
        """Split the deck into number_of_hands amount of card groups"""
        hands = []
        for hand_index in range(number_of_hands):
            starting_index = 0 + hand_index
            hands.append(CardDeck(self.cards[starting_index::number_of_hands]))
        return hands

    def draw(self, number_of_cards: int = 1) -> List[Card]:
        """Draw number_of_cards amount of cards from the deck (defaulted to 1)"""
        drawn_cards = []
        for _ in range(number_of_cards):
            drawn_cards.append(self.cards.pop(0))
        return drawn_cards

    def add(self, cards: List[Card]) -> None:
        """Add cards to the end of the deck"""
        self.cards.extend(cards)

    def __str__(self):
        """
        Print all the cards in the deck, in groups of 5 at a time, from the top of the deck (left) to the bottom (right).
        Card group amounts can be increased/decreased by changing the value of 'chunks'
        """
        res = ''
        chunks = 5
        for card_group in (self.cards[index:index + chunks] for index in range(0, len(self.cards), chunks)):
            strings = [str(card) for card in card_group]
            strings_by_column = [s.split('\n') for s in strings]
            strings_by_line = zip(*strings_by_column)

            for parts in strings_by_line:
                res += ''.join(parts) + '\n'

        return res
