class Mapper(object):
    def __init__(self, map_func, orchestrator):
        self.map = map_func
        self.orchestrator = orchestrator

    async def run(self, file_path):
        for data in self.map(file_path):
            await self.emit(data)

    async def emit(self, data):
        await self.orchestrator.receive(data)
