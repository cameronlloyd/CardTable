from .card import Card
from .card_deck import CardDeck
from typing import List


class Player:
    """
    A class to represent a person playing the card game

    Attributes
    ----------
    name: str
        First name of the player
    hand: CardDeck
        The player's hand dealt to them
    play_pile: CardDeck
        The player's cards in play for the current game/round
    """

    def __init__(self, name: str):
        self.name = name
        self.hand = None
        self.play_pile = None

    def add_to_hand(self, cards: List[Card], face_down: bool = False) -> None:
        """
        Add the provided cards to the end of this player's hand, all face down if specified, if one exists
        Otherwise, set up the player's hand using the cards provided
        """
        if not self.hand:
            self.hand = CardDeck(cards)
        else:
            if face_down:
                for card in cards:
                    card.face_up = False
            self.hand.add(cards)

    def add_to_play_pile(self, cards: List[Card]) -> None:
        """
        Add the provided cards to the end of the play_pile's card deck if one exists
        Otherwise, set up the play pile using the cards provided
        """
        if not self.play_pile:
            self.play_pile = CardDeck(cards)
        else:
            self.play_pile.add(cards)

    def clear_play_pile(self) -> None:
        """Reset the pile pile card stack to the default value"""
        self.play_pile = None

    def has_empty_hand(self) -> bool:
        """Check if this player's hand is empty"""
        return not self.hand or self.hand and self.hand.card_count() == 0

    def hand_count(self) -> int:
        """Count the number of cards in this player's hand"""
        if self.hand:
            return self.hand.card_count()
        return 0

    def draw_from_hand(self, number_of_cards: int = 1) -> List[Card]:
        """Draw the specified number_of_cards from this player's hand"""
        return self.hand.draw(number_of_cards)

    def __str__(self):
        """Print player name and card_count"""
        card_count = self.hand.card_count() if self.hand else 0
        return f'Name: {self.name}, Card Count: {card_count}'
