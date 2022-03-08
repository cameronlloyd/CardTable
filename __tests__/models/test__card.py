import unittest

from enums import Rank, Suit
from models import Card


class TestCard(unittest.TestCase):

    def test__init__valid(self):
        exp_rank = Rank.ACE
        exp_suit = Suit.DIAMONDS

        valid_card_1 = Card(exp_rank, exp_suit)
        valid_card_2 = Card(exp_rank, exp_suit, face_up=True)

        self.assertEqual(exp_rank, valid_card_1.rank)
        self.assertEqual(exp_suit, valid_card_1.suit)
        self.assertFalse(valid_card_1.face_up)

        self.assertEqual(exp_rank, valid_card_2.rank)
        self.assertEqual(exp_suit, valid_card_2.suit)
        self.assertTrue(valid_card_2.face_up)

    def test__init__invalid_rank(self):
        with self.assertRaises(Exception) as context:
            Card('FOOBAR', Suit.DIAMONDS)
        self.assertTrue('FOOBAR is not a valid rank' in str(context.exception))

    def test__init__invalid_suit(self):
        with self.assertRaises(Exception) as context:
            Card(Rank.ACE, 'FOOBAR')
        self.assertTrue('FOOBAR is not a valid suit' in str(context.exception))

    def test_flip(self):
        card = Card(Rank.KING, Suit.HEARTS)

        self.assertFalse(card.face_up)
        card.flip()
        self.assertTrue(card.face_up)
