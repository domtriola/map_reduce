class Mapper(object):
    def __init__(self, map_func, orchestrator):
        self.map = map_func
        self.orchestrator = orchestrator

    async def run(self, file_path):
        for data in self.map(file_path):
            self.emit(data)

    def emit(self, data):
        self.orchestrator.receive(data)
