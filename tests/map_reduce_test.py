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

class TestMapReduceSmall(unittest.TestCase):
    # TODO: Figure out how to run more than one test at a time:
    # RuntimeError: There is no current event loop in thread 'MainThread'.

    # def test_it_handles_card_counting_with_small_inputs(self):
    #     result = run_with_stack_path('seeds/small')
    #     expected = {
    #         'Hearts': 26,
    #         'Clubs': 13,
    #         'Spades': 9,
    #     }
    #     self.assertEqual(result, expected)

    # def test_it_handles_card_counting_with_medium_inputs(self):
    #     result = run_with_stack_path('seeds/medium')
    #     expected = {'Spades': 3271, 'Hearts': 3032, 'Diamonds': 3148, 'Clubs': 3054}
    #     self.assertEqual(result, expected)

    def test_it_handles_card_counting_with_large_inputs(self):
        result = run_with_stack_path('seeds/large')
        expected = {'Spades': 21203, 'Hearts': 20848, 'Diamonds': 20866, 'Clubs': 21115}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
