import os
import asyncio
import unittest

from map_reduce.map_reduce import MapReduce
from examples.counting_cards.counting_cards import map_func
from examples.counting_cards.counting_cards import reduce_func

def run_with_stack_path(rel_stack_dir):
    stack_dir = os.path.join(os.path.dirname(__file__), rel_stack_dir)
    file_paths = [os.path.join(stack_dir, stack)
                    for stack in os.listdir(stack_dir)]
    map_reduce = MapReduce(file_paths, map_func, reduce_func)
    return asyncio.run(map_reduce.run())

class TestMapReduce(unittest.TestCase):
    def test_it_handles_card_counting_with_small_inputs(self):
        result = run_with_stack_path('seeds/small')
        expected = {
            'Hearts': 26,
            'Clubs': 13,
            'Spades': 9,
        }
        self.assertEqual(result, expected)

    def test_it_handles_card_counting_with_large_inputs(self):
        result = run_with_stack_path('seeds/large')
        expected = {
            'Hearts': 5212,
            'Clubs': 5255,
            'Spades': 5313,
            'Diamonds': 5296
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
