from time import time


class CalculateFPS:

    start_time = time()
    counter = 0

    def calculte(self):
        self.counter += 1
        now = time()
        if now - self.start_time > 600:  # 00 = 60*10 which is 5 minutes
            self.counter = 1
            self.start_time = time()
        return int(self.counter/(now - self.start_time))


class DoEach:
    counter = 0
    times = 1

    def __init__(self, times, counter_init=0):
        super().__init__()
        self.times = times
        self.counter = counter_init

    def should_do(self):
        if self.counter % self.times == 0:
            self.counter += 1
            return True
        else:
            self.counter += 1
            return False

    def do(self, func, arg):
        if self.should_do():
            return func(arg)
        else:
            return None

    def do_async(self, pool, func, arg):
        if self.should_do():
            return pool.apply_async(func, (arg, ))
        else:
            return None
