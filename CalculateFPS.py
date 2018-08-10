from time import time


class CalculateFPS:

    start_time = time()
    counter = 0

    def calculte(self):
        counter += 1
        return int(self.counter/(time() - self.start_time))


class DoEach:
    counter = 0
    times = 1

    def __init__(self, times):
        super().__init__()
        self.times = 1
        self.counter = 0

    def do(self, func, args=()):
        args = list(args)
        self.counter += 1
        if self.counter % self.times == 0:
            return func(*args)

    def do_async(self, pool, func, args=()):
        pool.apply_async(self.do(func, args))
