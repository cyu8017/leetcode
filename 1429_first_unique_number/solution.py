from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums):
        self.counts = {}
        self.unique = OrderedDict()
        for value in nums:
            self.add(value)

    def showFirstUnique(self):
        return next(iter(self.unique), -1)

    def add(self, value):
        self.counts[value] = self.counts.get(value, 0) + 1
        if self.counts[value] == 1:
            self.unique[value] = None
        else:
            self.unique.pop(value, None)
