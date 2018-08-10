from time import time


class CalculateFPS:

    start_time = time()
    counter = 0

    def calculte(self):
        self.counter += 1.0
        return self.counter/(time() - self.start_time)


class DoEach:
    counter = 0
    times = 1

    def __init__(self, times):
        super().__init__()
        self.times = 1
        self.counter = 0

    def do(self, func, arg):
        self.counter += 1
        if self.counter % self.times == 0:
            return func(arg)

    def do_async(self, pool, func, arg):
        pool.apply_async(self.do(func, arg))
