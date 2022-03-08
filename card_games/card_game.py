import os

from models import Card, CardDeck, Player
from typing import List


class CardGame:
    """
    A class representing an executable card game

    Attributes
    ----------
    number_of_players: int
        The number of Players playing the game
    players: List[Player]
        The players playing the game
    round_number: int
        The current round number of the game being executed
    round_winner: Player
        The winner of the current round
    game_winner: Player
        The winner of the game
    """

    def __init__(self, players: List[Player]):
        self.number_of_players = len(players)
        self.players = players
        self.round_number = 0
        self.round_winner = None
        self.game_winner = None

    def deal_hands(self) -> None:
        """Deal the standard 52 card deck to each player"""
        hands = CardDeck().deal(self.number_of_players)
        for player_number, hand in enumerate(hands):
            self.players[player_number].hand = hand

    def play_top_card(self, player: Player) -> Card or None:
        """Pull the top card from the player's hand, set it face up, and to the play pile"""
        if player.hand and player.hand_count() > 0:
            drawn_card = player.draw_from_hand()[0]
            drawn_card.flip()
            player.add_to_play_pile([drawn_card])
            return drawn_card
        return None

    def shuffle_hand_if_needed(self, player: Player) -> None:
        """Shuffle the player's hand if the top card is face up, meaning all cards in deck have been played"""
        if player.hand.cards[0].face_up:
            print(f'Shuffling {player.name}\'s deck...\n')
            player.hand.shuffle()

    def end_round(self) -> None:
        """Display round summary and reset round variables"""
        self.print_round_summary()
        for player in self.players:
            player.clear_play_pile()
        self.round_winner = None

    def end_game(self) -> None:
        """Display game summary and reset game variables"""
        self.print_game_summary()
        for player in self.players:
            player.hand = None
        self.game_winner = None
        self.round_number = 0

    def print_round_plays(self) -> None:
        """Print the card's in each player's play_pile this round"""
        for player in self.players:
            print(f'{player.name} plays:\n{player.play_pile}')

    def print_round_summary(self) -> None:
        """Print a summary of the current round to user"""
        self.round_number += 1
        print(f'ROUND {self.round_number} RESULTS')
        print('-------------------------')
        print(f'Winner: {self.round_winner.name}')
        for player in self.players:
            print(f'{player.name}\'s card count: {player.hand_count()}')

    def print_game_summary(self) -> None:
        """Print the final game summary to user"""
        print(f'\n\n=============GAME OVER!=============\n')
        print(f'GAME SUMMARY')
        print('----------------------------')
        print(f'Winner: {self.game_winner.name}')
        print(f'Number of rounds: {self.round_number}')

    def clear_prompt(self) -> None:
        """Clear user prompt"""
        os.system("cls")
