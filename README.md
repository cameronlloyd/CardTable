# CardTable

CardTable is an interactive launcher for various card games. For the time being, CardTable only includes the card game [War](#war)

## Running CardTable

From a terminal in project's main directory, run the command:

```bash
python run.py
```

From the prompt, enter the menu item number of the game you would like to play.

## Running Tests

From a terminal in project's main directory, run the command:

```bash
python run_tests.py
```

The results of all unit tests will be displayed in the terminal

## Card Games

### War

This version of war was built using the rules defined by [Wikipedia](<https://en.wikipedia.org/wiki/War_(card_game)#Gameplay>).<br/>

A few notes about this version that aren't specified in the gameplay instructions at the link above:

1. This version uses a standard 52-card deck, with Jokers removed
2. If a player doesn't have enough cards (4) for a "war", then the game ends and said player automatically loses.
3. Card's won during a round by a player are put face up at the bottom of the winning player's deck. At the start of each round, if the top card on the player's deck is face up, then all cards will be put face down and the hand will be shuffled.
    - Note: without this shuffling I noticed scenarios where the game would go on for an extremely large (>1000) amount of rounds.  Shuffling seems to reduce the chance of entering a state where one hand's Ace stays unchallenged for a long amount of time.

## Developer Notes

### Regrets

1. I didn't notice the point in the instructions about adding several commits to the git history until the project was complete.  I tried commiting in chunks, but I recognize this is not the same, and I appologize
2. Not purchasing a real deck of cards to practice War before/during development

### Possible Future Improvements:

1. The current folder structure isn't exactly intuitive or well thought out. Next steps would be to rethink the folder structuring.
2. Testing improvements:
    - Implement a testing framework such as [pytest](https://docs.pytest.org/en/7.0.x/) instead of just the standard python unittesting framework
    - Add dedicated tests around the \_\_str\_\_ methods. These tests are currently either ignoring the user output or not checking it
    - Add some better patching/mocking to decouple test classes
    - Overall more testing. Currently the CardTable class isn't being tested
3. Validation improvents:
    - Type hinting is currently being used in this project, but almost all method parameters aren't being validated. This would need to be improved in the future
4. It might make sense to replace some things like the user prompting with a fully featured 3rd party package
5. Add a user interface, or at least update some of the prompting and ASCII art
