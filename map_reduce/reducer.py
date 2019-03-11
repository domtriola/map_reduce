class Reducer(object):
    def __init__(self, reduce_func, orchestrator):
        self.reduce = reduce_func
        self.orchestrator = orchestrator

    async def run(self, key, values):
        await self.emit((key, self.reduce(values)))

    async def emit(self, data):
        await self.orchestrator.receive(data)
