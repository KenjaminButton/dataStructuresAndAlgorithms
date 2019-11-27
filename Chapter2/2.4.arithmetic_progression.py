class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

    
# Inherit from Progression.
class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

# A class that produces a geometric progression.
class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

# A class that produces Fibonacci progression.
class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


if name == __main__ : 
    print('Default progression: ')
    Progression().print_progression(10)
    
    print('Arithmetic progression with increment 5: ')
    ArithmeticProgression(5).print_progression(10)
    
    print('Arithmetic progression with increment 5 and start 2: ')
    ArithmeticProgression(5, 2).print_progression(10)
    
    print('Geometric progression with default base: ')
    GeometricProgression().print_progression(10)
    
    print('Geometric progression with base 3: ')
    GeometricProgression(3).print_progression(10)
    
    print('Fibonacci progression with default start values: ')
    FibonacciProgression().print_progression(10)
    
    print('Fibonacci progression with start values 4 and 6: ')
    FibonacciProgression(4, 6).print_progression(10)


"""
Code Fragment 2.13: Output of the unit tests from Code Fragment 2.12.

Default progression:
0123456789
Arithmetic progression with increment 5:
0 5 10 15 20 25 30 35 40 45
Arithmetic progression with increment 5 and start 2: 2 7 12 17 22 27 32 37 42 47
Geometric progression with default base:
1 2 4 8 16 32 64 128 256 512
Geometric progression with base 3:
1 3 9 27 81 243 729 2187 6561 19683
Fibonacci progression with default start values:
0 1 1 2 3 5 8 13 21 34
Fibonacci progression with start values 4 and 6:
4 6 10 16 26 42 68 110 178 288
"""