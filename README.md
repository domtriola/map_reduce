# Mock MapReduce

## Overview

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

## TODO

### Implement a more robust solution so chunks of work can be given to reducers before a mapper has parsed all data.

The first implementation I had would queue up reducers with chunks of work as data from the mappers came in. That would work for relatively small inputs of ~<1000 lines per file. But data would go missing with large inputs, because of a race condition with the shared mapped data state. By adding locks I was able to acheive the expected result, but the reducers are no longer initialized until all of the mappers are done.
