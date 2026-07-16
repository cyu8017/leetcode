class MRUQueue:
    def __init__(self, n):
        self.q = list(range(1, n + 1))
    def fetch(self, k):
        val = self.q.pop(k - 1)
        self.q.append(val)
        return val
