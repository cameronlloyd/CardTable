import unittest

from enums import Rank, Suit
from models import Card, CardDeck


class TestCardDeck(unittest.TestCase):

    def test__init(self):
        deck = CardDeck()
        self.assertTrue(52, len(deck.cards))

        cards = [Card(Rank.FOUR, Suit.SPADES)]
        deck_2 = CardDeck(cards)
        self.assertEqual(cards, deck_2.cards)

    def test__card_count(self):
        cards = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        deck = CardDeck(cards)
        self.assertEqual(len(cards), deck.card_count())

    def test__deal(self):
        deck = CardDeck()
        hands = deck.deal(2)
        self.assertEqual(2, len(hands))
        self.assertEqual(26, len(hands[0].cards))
        self.assertEqual(26, len(hands[1].cards))

        deck = CardDeck()
        hands = deck.deal(3)
        self.assertEqual(3, len(hands))
        self.assertEqual(18, len(hands[0].cards))
        self.assertEqual(17, len(hands[1].cards))
        self.assertEqual(17, len(hands[2].cards))

    def test__draw(self):
        deck = CardDeck()
        first_card = deck.cards[0]
        second_card = deck.cards[1]
        third_card = deck.cards[2]

        self.assertEqual(52, len(deck.cards))

        drawn_cards = deck.draw(3)
        self.assertEqual(49, len(deck.cards))
        self.assertEqual(first_card, drawn_cards[0])
        self.assertEqual(second_card, drawn_cards[1])
        self.assertEqual(third_card, drawn_cards[2])

    def test__add(self):
        card_1 = Card(Rank.FOUR, Suit.SPADES)
        deck = CardDeck([card_1])

        self.assertEqual(1, len(deck.cards))

        card_2 = Card(Rank.EIGHT, Suit.SPADES)
        deck.add([card_2])
        self.assertEqual(2, len(deck.cards))
        self.assertEqual(card_2, deck.cards[-1])


