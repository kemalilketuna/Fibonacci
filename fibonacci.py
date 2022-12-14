class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        r = self.a
        self.a, self.b = self.b, self.a + self.b
        return r
    
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 0, 1
            L = []
            if stop is not None:
                for _ in range(stop):
                    if _ >= start:
                        L.append(a)
                    a, b = b, a + b
                return L
            else:
                raise ValueError('stop is None')
