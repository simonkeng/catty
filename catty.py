import time
import numpy as np

def print_catty(catty):
    print('  ', catty, end='\r')

class Catty:
    def __init__(self):
        self._expression = '=^.^='

    def __str__(self):
        return self._expression

    def set_expression(self, new):
        self._expression = new
        print_catty(self)

    def run(self):
        while True:
            self.set_expression('=-.-=')
            time.sleep(np.random.uniform(0.1, 0.7))
            self.set_expression('=0.0=')
            time.sleep(np.random.uniform(0.08, 0.5))
            self.set_expression('=^.^=')
            time.sleep(np.random.uniform(0.7, 2))
            self.set_expression('>^.^<')
            time.sleep(np.random.uniform(0.02, 0.4))
            self.set_expression('>0.0<')
            time.sleep(np.random.uniform(0.01, 0.3))

cat = Catty()
cat.run()

