import os
import random
from examples.counting_cards.card import Card

if __name__ == '__main__':
    stack_dir = os.path.join(os.path.dirname(__file__), 'card_stacks')

    for stack_key in ['a', 'b', 'c']:
        filepath = os.path.join(stack_dir, 'stack_{}.txt'.format(stack_key))
        with open(filepath, 'w+') as f:
            for _ in range(200):
                f.write('{value} {suit}\n'.format(
                    value=random.choice(list(Card.VALUES.keys())),
                    suit=random.choice(Card.SUITS)
                ))
