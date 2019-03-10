# Mock MapReduce

As an exploration of MapReduce I made this over-simplified implementation of MapReduce in Python. It doesn't really process things in parallel, and it is missing some key functionality of what makes MapReduce really useful, but it demonstrates at least some of the basic idea of how MapReduce works.

Run example:
```bash
python3 -m examples.counting_cards.counting_cards
```

Generate new seed data:
```bash
python3 -m examples.counting_cards.generate_card_stacks
```

Example output:
```bash
(venv) dominicks-air:map-reduce dominicktriola$ python3 -m examples.counting_cards.counting_cards
Initializing all mappers
Map worker created for: /Users/dominicktriola/src/map-reduce/examples/counting_cards/card_stacks/stack_c.txt
Map worker created for: /Users/dominicktriola/src/map-reduce/examples/counting_cards/card_stacks/stack_b.txt
Map worker created for: /Users/dominicktriola/src/map-reduce/examples/counting_cards/card_stacks/stack_a.txt
Waiting for map tasks to finish
Creating reducer for key: Hearts, values: [3, 10, 10, 1, 8, 5, 2, 3, 6, 5]
Creating reducer for key: Spades, values: [5, 12, 1, 11, 4, 8, 10, 12, 3, 2]
Creating reducer for key: Diamonds, values: [3, 2, 7, 11, 8, 13, 4, 8, 13, 13]
Creating reducer for key: Clubs, values: [6, 9, 7, 9, 6, 2, 6, 7, 13, 8]
Creating reducer for key: Spades, values: [1, 8, 13, 1, 4, 11, 3, 5, 4, 2]
Creating reducer for key: Diamonds, values: [6, 3, 7, 10, 13, 10, 10, 7, 9, 2]
Creating reducer for key: Spades, values: [12, 8, 7, 3, 13, 3, 13, 5, 4, 6]
Creating reducer for key: Hearts, values: [12, 9, 12, 11, 12, 13, 3, 13, 5, 4]
Creating reducer for key: Clubs, values: [6, 3, 5, 8, 3, 4, 3, 1, 6, 11]
Creating reducer for key: Diamonds, values: [11, 5, 6, 5, 12, 1, 3, 1, 2, 3]
Creating reducer for key: Hearts, values: [5, 12, 9, 11, 7, 2, 12, 12, 9, 5]
Creating reducer for key: Spades, values: [8, 12, 8, 4, 12, 6, 4, 6, 3, 8]
Creating reducer for key: Clubs, values: [9, 8, 3, 6, 11, 1, 6, 12, 2, 11]
Creating reducer for key: Diamonds, values: [4, 5, 2, 2, 3, 2, 8, 1, 10, 1]
Creating reducer for key: Clubs, values: [13, 8, 1, 8, 13, 10, 5, 6, 7, 3]
Creating reducer for key: Hearts, values: [6, 4, 7, 8, 12, 6, 13, 2, 2, 11]
Creating reducer for key: Spades, values: [8, 7, 12, 3, 3, 1, 10, 5, 9, 4]
Creating reducer for key: Diamonds, values: [10, 2, 2, 12, 12, 8, 8, 3, 13, 6]
Creating reducer for key: Hearts, values: [7, 3, 8, 2, 8, 4, 5, 5, 3, 8]
Creating reducer for key: Diamonds, values: [7, 9, 9, 3, 10, 2, 5, 7, 11, 5]
Creating reducer for key: Spades, values: [2, 8, 12, 7, 2, 3, 10, 7, 13, 2]
Creating reducer for key: Hearts, values: [3, 12, 4, 7, 6, 1, 6, 13, 12, 8]
Creating reducer for key: Clubs, values: [9, 8, 8, 8, 1, 8, 10, 12, 7, 12]
Creating reducer for key: Spades, values: [11, 6, 4, 4, 8, 7, 7, 6, 8, 12]
Creating reducer for key: Clubs, values: [2, 3, 12, 4, 13, 6, 10, 6, 3, 13]
Creating reducer for key: Diamonds, values: [13, 3, 13, 8, 12, 8, 2, 10, 6, 12]
Creating reducer for key: Hearts, values: [7, 8, 9, 6, 6, 11, 8, 1, 6, 1]
Creating reducer for key: Spades, values: [10, 9, 1, 6, 7, 8, 2, 10, 7, 10]
Creating reducer for key: Diamonds, values: [12, 9, 3, 8, 10, 4, 9, 5, 5, 12]
Creating reducer for key: Clubs, values: [8, 8, 4, 10, 8, 10, 3, 11, 10, 12]
Creating reducer for key: Spades, values: [8, 7, 1, 11, 5, 10, 10, 8, 2, 10]
Creating reducer for key: Hearts, values: [11, 12, 1, 12, 7, 6, 10, 3, 9, 1]
Creating reducer for key: Clubs, values: [10, 13, 1, 8, 3, 13, 1, 7, 7, 2]
Creating reducer for key: Spades, values: [6, 10, 11, 5, 10, 5, 9, 7, 2, 8]
Creating reducer for key: Diamonds, values: [12, 13, 13, 8, 1, 2, 10, 12, 8, 10]
Creating reducer for key: Hearts, values: [9, 12, 12, 10, 8, 12, 6, 11, 9, 5]
Creating reducer for key: Clubs, values: [3, 3, 9, 2, 9, 10, 5, 4, 5, 2]
Creating reducer for key: Spades, values: [12, 1, 2, 3, 8, 3, 11, 4, 11, 11]
Creating reducer for key: Hearts, values: [12, 3, 3, 5, 3, 9, 4, 1, 4, 12]
Creating reducer for key: Diamonds, values: [6, 9, 3, 12, 6, 1, 13, 6, 12, 9]
Creating reducer for key: Spades, values: [12, 13, 13, 8, 5, 7, 8, 1, 1, 12]
Creating reducer for key: Clubs, values: [4, 8, 1, 2, 8, 3, 13, 6, 4, 11]
Creating reducer for key: Hearts, values: [1, 9, 4, 3, 5, 7, 8, 5, 4, 2]
Creating reducer for key: Diamonds, values: [9, 13, 8, 10, 4, 10, 8, 8, 2, 9]
Creating reducer for key: Clubs, values: [13, 10, 8, 7, 13, 5, 2, 6, 10, 12]
Creating reducer for key: Hearts, values: [2, 10, 6, 6, 9, 13, 9, 1, 7, 4]
Creating reducer for key: Diamonds, values: [11, 8, 12, 9, 10, 10, 5, 3, 5, 4]
Creating reducer for key: Spades, values: [9, 10, 1, 8, 7, 11, 8, 5, 6, 6]
Creating reducer for key: Hearts, values: [12, 12, 9, 3, 1, 2, 2, 10, 7, 1]
Creating reducer for key: Diamonds, values: [1, 4, 4, 4, 7, 5, 9, 11, 4, 10]
Creating reducer for key: Clubs, values: [4, 8, 8, 10, 2, 9, 2, 12, 3, 7]
Creating reducer for key: Spades, values: [8, 8, 12, 8, 11, 10, 13, 1, 10, 1]
Creating reducer for key: Diamonds, values: [5, 12, 1, 8, 6, 12, 9, 12, 11, 9]
Creating reducer for key: Hearts, values: [1, 4, 8, 8, 7, 13, 11, 12, 1, 12]
Creating reducer for key: Spades, values: [10, 1, 1, 4, 4, 4, 12, 8, 5, 7]
Creating reducer for key: Clubs, values: [12, 3, 5, 1, 5, 1, 8, 2, 9, 7]
Creating reducer for key: Diamonds, values: [11, 12, 6, 5, 5, 9, 10, 2, 6, 3]
Creating reducer for key: Hearts, values: [4, 3, 3, 7, 9, 13, 11, 6, 5, 8]
Creating reducer for key: Diamonds, values: [3, 9, 4, 8, 10, 11, 2, 9, 82, 77]
Creating reducer for key: Spades, values: [10, 11, 1, 8, 8, 68, 52, 74, 71, 62]
Creating reducer for key: Clubs, values: [11, 7, 11, 9, 11, 73, 50, 69, 74, 83]
Creating reducer for key: Hearts, values: [8, 13, 53, 94, 84, 71, 53, 72, 63, 72]
Creating reducer for key: Diamonds, values: [49, 38, 76, 68, 87, 77, 89, 77, 81, 77]
Creating reducer for key: Spades, values: [66, 73, 70, 72, 73, 66, 80, 71, 82, 56]
All map tasks finished
Waiting for all tasks to finish
Flushing all data
Creating reducer for key: Clubs, values: [72, 84, 65, 52, 60, 86, 65, 53, 398]
Creating reducer for key: Spades, values: [365, 709]
Creating reducer for key: Hearts, values: [94, 56, 48, 67, 59, 77, 69, 583]
Creating reducer for key: Diamonds, values: [59, 85, 69, 215, 719]
Waiting for final tasks
All reduce tasks finished
Clubs: 935
Spades: 1074
Hearts: 1053
Diamonds: 1147
```
