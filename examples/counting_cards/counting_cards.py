"""
Given a stack of cards calculate the total value for each suit.

Input: a file with a list of files that contain cards listed in the form:
<value> <suit>
<value> <suit>
<value> <suit>
etc.
"""

import os
import asyncio
import functools
from map_reduce.map_reduce import MapReduce
from examples.counting_cards.card import Card

def map_func(file_path):
    with open(file_path) as f:
        for line in f:
            value, suit = line.strip().split(' ')
            yield (suit, Card.VALUES[value])

def reduce_func(values):
    return functools.reduce(lambda a, b: a + b, values)

if __name__ == '__main__':
    stack_dir = os.path.join(os.path.dirname(__file__), 'card_stacks')
    file_paths = [os.path.join(stack_dir, stack) for stack in os.listdir(stack_dir)]
    map_reduce = MapReduce(file_paths, map_func, reduce_func, verbose=True)

    result = asyncio.run(map_reduce.run())
    print('\nResults:')
    for key, value in result.items():
        print('{key}: {value}'.format(key=key, value=value))
