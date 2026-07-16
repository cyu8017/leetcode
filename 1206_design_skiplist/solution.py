from bisect import bisect_left, insort

class Skiplist:
    def __init__(self):
        self.values = []

    def search(self, target: int) -> bool:
        i = bisect_left(self.values, target)
        return i < len(self.values) and self.values[i] == target

    def add(self, num: int) -> None:
        insort(self.values, num)

    def erase(self, num: int) -> bool:
        i = bisect_left(self.values, num)
        if i == len(self.values) or self.values[i] != num: return False
        self.values.pop(i)
        return True
