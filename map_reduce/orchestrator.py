import asyncio
from map_reduce.mapper import Mapper
from map_reduce.reducer import Reducer

class Orchestrator(object):
    """
    An ultra-simplified implementation of MapReduce.

    This implementation runs workers concurrently, not in parallel. So there's
    no real performance benefit. It also does not reduce in parallel.

    TODO: The orchestrator is acting as an orchestrator and a worker. Distribute
    the work to nodes, so the orchestrator can keep processing distinct results
    until the final aggregation is acheived (rather than assuming we'll have all
    the necessary aggregations after one mapping).
    """

    def __init__(self, file_paths, map_func, reduce_func):
        self.file_paths = file_paths
        self.mapper = Mapper(map_func)
        self.reducer = Reducer(reduce_func)
        self.worker_tasks = []
        self.reducer_tasks = []

    async def run(self):
        key_value_sets = await self.map()
        aggregations = self.aggregate(key_value_sets)

        results = {}
        for key, values in aggregations.items():
            k, value = self.reducer.run(key, values)
            results[k] = value
        return results

    async def map(self):
        for file_path in self.file_paths:
            worker_task = self.instantiate_worker(self.mapper, file_path)
            self.worker_tasks.append(worker_task)
        return await asyncio.gather(*self.worker_tasks)

    def instantiate_worker(self, worker_func, file_path):
        return asyncio.create_task(worker_func.run(file_path))

    @staticmethod
    def aggregate(key_value_sets):
        aggregations = {}
        for key_value_set in key_value_sets:
            for key, value in key_value_set:
                if key in aggregations:
                    aggregations[key].append(value)
                else:
                    aggregations[key] = [value]
        return aggregations
