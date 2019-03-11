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

Run Tests:
```bash
python3 -m tests.map_reduce_test
```
