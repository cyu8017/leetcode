from itertools import combinations

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.items = iter(map("".join, combinations(characters, combinationLength)))
        self.next_item = next(self.items, None)

    def next(self) -> str:
        current = self.next_item
        self.next_item = next(self.items, None)
        return current

    def hasNext(self) -> bool:
        return self.next_item is not None
