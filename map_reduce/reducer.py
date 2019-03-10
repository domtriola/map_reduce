class Reducer(object):
    def __init__(self, reduce_func):
        self.reduce = reduce_func

    def run(self, key, values):
        return (key, self.reduce(values))
