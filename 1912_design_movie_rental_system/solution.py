import bisect
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}
        self.available = {}
        self.rented = []
        for shop, movie, price in entries:
            self.price[(shop, movie)] = price
            self.available.setdefault(movie, [])
            bisect.insort(self.available[movie], (price, shop))

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.available.get(movie, [])[:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price[(shop, movie)]
        self.available[movie].remove((price, shop))
        bisect.insort(self.rented, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price[(shop, movie)]
        self.rented.remove((price, shop, movie))
        bisect.insort(self.available[movie], (price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]
