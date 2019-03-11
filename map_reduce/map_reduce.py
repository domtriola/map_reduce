import asyncio
from collections import deque
from map_reduce.mapper import Mapper
from map_reduce.reducer import Reducer

class Orchestrator(object):
    def __init__(self, reduce_func, print_if_verbose):
        self.lock = asyncio.Lock()
        self.mapped_data = {}
        self.reducer = Reducer(reduce_func, self)
        self.reducer_tasks = []
        self.print_if_verbose = print_if_verbose

    async def receive(self, data):
        key, value = data
        async with self.lock:
            if key in self.mapped_data:
                self.mapped_data[key].append(value)
                self.try_partition_to_reducer(key)
            else:
                self.mapped_data[key] = deque([value])

    async def try_partition_to_reducer(self, key):
        async with self.lock:
            if len(self.mapped_data[key]) >= 10:
                data_to_reduce = []
                for _ in range(10):
                    data_to_reduce.append(self.mapped_data[key].popleft())
                return self._create_reducer_task(key, data_to_reduce)

    async def flush(self):
        self.print_if_verbose('Flushing all data')
        for key, values in self.mapped_data.items():
            if len(values) > 1:
                data_to_reduce = []
                while len(values) > 0:
                    data_to_reduce.append(values.popleft())
                self._create_reducer_task(key, data_to_reduce)

        self.print_if_verbose('Waiting for final tasks')
        await asyncio.gather(*self.reducer_tasks)

    def _create_reducer_task(self, key, data):
        self.print_if_verbose('Creating reducer for key: {}, values: {}'.format(key, data))
        reducer_task = asyncio.create_task(
            self.reducer.run(key, data))
        self.reducer_tasks.append(reducer_task)
        return reducer_task

class MapReduce(object):
    """
    An ultra-simplified implementation of MapReduce.

    This implementation runs workers concurrently, not in parallel, so there's
    no real performance benefit.
    """

    def __init__(self, file_paths, map_func, reduce_func, verbose=False):
        self.verbose = verbose
        self.file_paths = file_paths
        self.orchestrator = Orchestrator(reduce_func, self.print_if_verbose)
        self.mapper = Mapper(map_func, self.orchestrator)
        self.map_tasks = []

    async def run(self):
        self.print_if_verbose('Initializing all mappers')
        self.instantiate_mappers()

        self.print_if_verbose('Waiting for map tasks to finish')
        await asyncio.gather(*self.map_tasks)
        self.print_if_verbose('All map tasks finished')

        await self.orchestrator.flush()
        self.print_if_verbose('All reduce tasks finished')

        return self.result()

    def instantiate_mappers(self):
        for file_path in self.file_paths:
            worker_task = self.instantiate_worker(self.mapper, file_path)
            self.print_if_verbose('Map worker created for: {}'.format(file_path))
            self.map_tasks.append(worker_task)
        return self.map_tasks

    def instantiate_worker(self, worker_func, file_path):
        return asyncio.create_task(worker_func.run(file_path))

    def result(self):
        return {key: values[0] for key, values in self.orchestrator.mapped_data.items()}

    def print_if_verbose(self, string):
        if self.verbose:
            print(string)
