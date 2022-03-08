import unittest

from card_games.card_game import CardGame
from models import Player


class TestCardGame(unittest.TestCase):

    def test__init(self):
        players = [Player('Player 1'), Player('Player 2')]
        game = CardGame(players)

        self.assertEqual(2, game.number_of_players)
        self.assertEqual(players, game.players)
        self.assertEqual(0, game.round_number)
        self.assertIsNone(game.round_winner)
        self.assertIsNone(game.game_winner)

    def test__deal_hands(self):
        players = [Player('Player 1'), Player('Player 2')]
        game = CardGame(players)

        game.deal_hands()
        self.assertEqual(26, game.players[0].hand.card_count())
        self.assertEqual(26, game.players[1].hand.card_count())

    def test__play_top_card(self):
        players = [Player('Player 1'), Player('Player 2')]
        game = CardGame(players)

        self.assertIsNone(game.play_top_card(players[0]))

        game.deal_hands()
        drawn_card = game.play_top_card(players[0])
        self.assertEqual(1, game.players[0].play_pile.card_count())
        self.assertEqual(drawn_card, game.players[0].play_pile.cards[0])
        self.assertTrue(drawn_card.face_up)
