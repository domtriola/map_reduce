class Mapper(object):
    def __init__(self, map_func):
        self.map = map_func

    async def run(self, file_path):
        return self.map(file_path)
