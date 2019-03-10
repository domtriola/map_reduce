class Reducer(object):
    def __init__(self, reduce_func, orchestrator):
        self.reduce = reduce_func
        self.orchestrator = orchestrator

    async def run(self, key, values):
        self.emit((key, self.reduce(values)))

    def emit(self, data):
        self.orchestrator.receive(data)
