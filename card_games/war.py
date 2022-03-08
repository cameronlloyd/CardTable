from card_games.card_game import CardGame
from enums import Rank
from models import Card, Player
from typing import List


class War(CardGame):
    """
    A class representing an executable version of the card game 'War'

    Attributes
    ----------
    war_count: int
        The number of 'War's that have happened this game
    player_one: Player
        The first player playing the game
    player_two: Player
        The second player playing the game
    rank_value_map: Dict[Rank, int]
        The card rank value associated with the Rank.  Higher numbers "beat" lower numbers head-to-head
    """

    def __init__(self):
        player_one_name = input(
            'Enter the name of player 1 - [default: Player 1]: ') or 'Player 1'
        player_two_name = input(
            'Enter the name of player 2 - [default: Player 2]: ') or 'Player 2'

        self.war_count = 0
        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)
        self.rank_value_map = {
            Rank.TWO: 2,
            Rank.THREE: 3,
            Rank.FOUR: 4,
            Rank.FIVE: 5,
            Rank.SIX: 6,
            Rank.SEVEN: 7,
            Rank.EIGHT: 8,
            Rank.NINE: 9,
            Rank.TEN: 10,
            Rank.JACK: 11,
            Rank.QUEEN: 12,
            Rank.KING: 13,
            Rank.ACE: 14,
        }

        super().__init__([self.player_one, self.player_two])

    def play(self) -> None:
        """
        Deal both players hands and play rounds of war until:
            1. A player has ran out of cards
            2. War was declared and a player doesn't have enough cards for War
        """
        self.deal_hands()

        skip_to_end = False
        while not self.game_winner:
            print(f'\n\t\tROUND {self.round_number + 1}\n')
            self.play_round()

            # If either player has ran out of cards then the other player wins
            if self.player_one.has_empty_hand():
                self.game_winner = self.player_two
            elif self.player_two.has_empty_hand():
                self.game_winner = self.player_one

            # Ask the user to either continue to next round or automate the game to the end
            if not skip_to_end and not self.game_winner:
                user_input = input(
                    '\nPress ENTER to continue or \'s\' to skip to end: ')
                if user_input == 's' or user_input == 'S':
                    skip_to_end = True

        # End game and ask user if they would like to play again
        self.end_game()
        print(f'Number of wars: {self.war_count}\n')
        self.prompt_replay()

    def play_round(self) -> None:
        """Play a round of war"""
        # Shuffle hand if the card on top of the deck for the player is face up, meaning all cards have been cycled
        self.shuffle_hand_if_needed(self.player_one)
        self.shuffle_hand_if_needed(self.player_two)

        # Update and display play piles for each player
        card_one = self.play_top_card(self.player_one)
        card_two = self.play_top_card(self.player_two)
        self.print_round_plays()

        # Determine round winner
        self.determine_round_winner([card_one], [card_two])

        # Print round results and clear both player's play piles
        self.end_round()

    def declare_war(self) -> None:
        """Play out a War"""
        print('Tie! Declare war!\n')
        self.war_count += 1

        # If either player has less the 4 cards required for war, then the game is over and the other player wins
        # Otherwise, determine a round winner using war cards
        if self.player_one.hand_count() < 4:
            self.game_winner = self.player_two
            self.round_winner = self.player_two
            print(f'{self.player_one.name} doesn\'t have enough cards for war...\n')
        elif self.player_two.hand_count() < 4:
            self.game_winner = self.player_one
            self.round_winner = self.player_one
            print(f'{self.player_two.name} doesn\'t have enough cards for war...\n')
        else:
            # Update and display war play piles for each player
            war_cards_one = self.play_war_cards(self.player_one)
            war_cards_two = self.play_war_cards(self.player_two)
            self.print_round_plays()

            # Determine round winner
            self.determine_round_winner(war_cards_one, war_cards_two)

    def play_war_cards(self, player: Player) -> List[Card]:
        """Draw 'War' cards for the provided player and put them in play.  Then return all cards pulled"""
        # Draw 3 cards and leave face down
        drawn_cards = player.draw_from_hand(3)

        # Draw 4th card, which is used to determine round winner, and flip it face up
        war_card = player.draw_from_hand()[0]
        war_card.flip()
        drawn_cards.append(war_card)

        # Add cards to play pile and return them
        player.add_to_play_pile(drawn_cards)
        return drawn_cards

    def determine_round_winner(self, cards_one: List[Card], cards_two: List[Card]) -> None:
        """
        Determine which player wins this round, or declare 'War' in the event of a tie

            Parameters:
                cards_one (List[Card]): The cards played by player one
                cards_two (List[Card]): The cards played by player two
        """

        # Pull the rightmost card from list
        decision_card_one = cards_one[-1]
        decision_card_two = cards_two[-1]

        # Check the value of both cards
        decision_card_one_value = self.rank_value_map[decision_card_one.rank]
        decision_card_two_value = self.rank_value_map[decision_card_two.rank]

        # Determine round winner or declare war if there's a tie
        if decision_card_one_value > decision_card_two_value:
            self.player_one.add_to_hand(self.player_one.play_pile.cards)
            self.player_one.add_to_hand(self.player_two.play_pile.cards)
            self.round_winner = self.player_one
        elif decision_card_one_value < decision_card_two_value:
            self.player_two.add_to_hand(self.player_one.play_pile.cards)
            self.player_two.add_to_hand(self.player_two.play_pile.cards)
            self.round_winner = self.player_two
        elif decision_card_one_value == decision_card_two_value:
            self.declare_war()

    def prompt_replay(self) -> None:
        """
        Ask user if they would like to play the game again, and reset and relaunch if so
        Otherwise, say farewell to the user
        """
        user_input = input('\nPress \'Y\' to play again: ')
        if user_input == 'Y' or user_input == 'y':
            self.war_count = 0
            self.clear_prompt()
            self.play()
        else:
            print('\nGoodbye!')
