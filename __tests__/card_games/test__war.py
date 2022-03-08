import io
import unittest
from unittest import mock
from unittest.mock import patch

from card_games import War
from enums import Rank, Suit
from models import Card


class TestWar(unittest.TestCase):

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    def test__init(self, mock_input):
        war = War()

        self.assertEqual(0, war.war_count)
        self.assertEqual('Player 1', war.player_one.name)
        self.assertEqual('Player 2', war.player_two.name)
        self.assertEqual(2, war.number_of_players)

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    def test__determine_round_winner__player_two_win(self, mock_input):
        war = War()
        war.deal_hands()

        cards_1 = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        cards_2 = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.KING, Suit.SPADES)]

        war.player_one.add_to_play_pile([cards_1[1]])
        war.player_two.add_to_play_pile([cards_2[1]])

        war.determine_round_winner(cards_1, cards_2)
        self.assertEqual(
            war.player_two.hand.cards[-2:], [cards_1[1], cards_2[1]])
        self.assertEqual(war.player_two, war.round_winner)

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    def test__determine_round_winner__player_one_win(self, mock_input):
        war = War()
        war.deal_hands()

        cards_1 = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        cards_2 = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.TWO, Suit.SPADES)]

        war.player_one.add_to_play_pile([cards_1[1]])
        war.player_two.add_to_play_pile([cards_2[1]])

        war.determine_round_winner(cards_1, cards_2)
        self.assertEqual(
            war.player_one.hand.cards[-2:], [cards_1[1], cards_2[1]])
        self.assertEqual(war.player_one, war.round_winner)

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    @patch('card_games.War.declare_war')
    def test__determine_round_winner__player_one_win(self, mock_input, mock_declare_war):
        war = War()
        war.deal_hands()

        cards_1 = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]
        cards_2 = [Card(Rank.FOUR, Suit.SPADES), Card(Rank.EIGHT, Suit.SPADES)]

        war.player_one.add_to_play_pile([cards_1[1]])
        war.player_two.add_to_play_pile([cards_2[1]])

        war.determine_round_winner(cards_1, cards_2)
        self.assertEqual(26, war.player_one.hand_count())
        self.assertIsNone(war.round_winner)

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    def test__play_war_cards(self, mock_input):
        war = War()
        war.deal_hands()

        drawn_cards = war.play_war_cards(war.player_one)

        self.assertEqual(4, len(drawn_cards))
        self.assertEqual(drawn_cards, war.player_one.play_pile.cards)
        self.assertFalse(drawn_cards[0].face_up)
        self.assertFalse(drawn_cards[1].face_up)
        self.assertFalse(drawn_cards[2].face_up)
        self.assertTrue(drawn_cards[3].face_up)

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    def test__declare_war__player_one_lose(self, mock_input):
        war = War()
        war.deal_hands()
        war.player_one.hand = None

        # Suppress print statement output
        with mock.patch('sys.stdout', new=io.StringIO()) as std_out:
            war.declare_war()
            self.assertEqual(1, war.war_count)
            self.assertEqual(war.player_two, war.game_winner)
            self.assertEqual(war.player_two, war.round_winner)

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    def test__declare_war__player_two_lose(self, mock_input):
        war = War()
        war.deal_hands()
        war.player_two.hand = None

        # Suppress print statement output
        with mock.patch('sys.stdout', new=io.StringIO()) as std_out:
            war.declare_war()
            self.assertEqual(1, war.war_count)
            self.assertEqual(war.player_one, war.game_winner)
            self.assertEqual(war.player_one, war.round_winner)

    @patch('builtins.input', side_effect=['Player 1', 'Player 2'])
    @patch('card_games.War.determine_round_winner')
    @patch('card_games.War.play_war_cards')
    def test__declare_war__player_two_lose(self, mock_input, mock_determine_winner, mock_play_war):
        war = War()
        war.deal_hands()

        # Suppress print statement output
        with mock.patch('sys.stdout', new=io.StringIO()) as std_out:
            war.declare_war()
            self.assertEqual(1, war.war_count)
            self.assertIsNone(war.game_winner)
            self.assertIsNone(war.round_winner)
