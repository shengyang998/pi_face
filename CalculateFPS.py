from time import time


class CalculateFPS:

    last_time = time()

    def calculte(self):
        fps = int(1.0/(time() - self.last_time))
        self.last_time = time()
        return fps


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
