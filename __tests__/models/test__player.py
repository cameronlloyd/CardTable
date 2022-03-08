import unittest

from enums import Rank, Suit
from models import Card, Player


class TestPlayer(unittest.TestCase):

    def test__init(self):
        name = 'FOOBAR'
        player = Player(name)

        self.assertEqual(name, player.name)
        self.assertIsNone(player.hand)
        self.assertIsNone(player.play_pile)

    def test__add_to_hand(self):
        player = Player('FOOBAR')
        cards = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]

        self.assertIsNone(player.hand)
        player.add_to_hand(cards)
        self.assertEqual(cards, player.hand.cards)

        cards_2 = [
            Card(Rank.FOUR, Suit.CLUBS, face_up=True),
            Card(Rank.EIGHT, Suit.CLUBS, face_up=True)
        ]
        player.add_to_hand(cards_2, face_down=True)
        self.assertFalse(player.hand.cards[-1].face_up)

    def test__add_to_play_pile(self):
        player = Player('FOOBAR')
        cards = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]

        self.assertIsNone(player.play_pile)
        player.add_to_play_pile(cards)
        self.assertEqual(cards, player.play_pile.cards)

        cards_2 = [
            Card(Rank.FOUR, Suit.CLUBS),
            Card(Rank.EIGHT, Suit.CLUBS)
        ]
        player.add_to_play_pile(cards_2)
        self.assertEqual(cards_2, player.play_pile.cards[-2:])
        self.assertFalse(player.play_pile.cards[-1].face_up)

    def test__clear_play_pile(self):
        player = Player('FOOBAR')
        cards = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        player.add_to_play_pile(cards)

        self.assertEqual(cards, player.play_pile.cards)
        player.clear_play_pile()
        self.assertIsNone(player.play_pile)

    def test__clear_play_pile(self):
        player = Player('FOOBAR')
        self.assertTrue(player.has_empty_hand())

        cards = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        player.add_to_hand(cards)
        self.assertFalse(player.has_empty_hand())

    def test__clear_play_pile(self):
        player = Player('FOOBAR')
        self.assertEqual(0, player.hand_count())

        cards = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        player.add_to_hand(cards)
        self.assertEqual(2, player.hand_count())

    def test__clear_play_pile(self):
        player = Player('FOOBAR')
        cards = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        player.add_to_hand(cards)
        drawn_cards = player.draw_from_hand(2)
        self.assertEqual(2, len(drawn_cards))
