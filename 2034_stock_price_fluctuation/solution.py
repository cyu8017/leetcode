# LeetCode 2034 - Stock Price Fluctuation
# https://leetcode.com/problems/stock-price-fluctuation/

import heapq


class StockPrice:
    def __init__(self):
        self.latest_ts = 0
        self.price_at = {}
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.price_at[timestamp] = price
        if timestamp >= self.latest_ts:
            self.latest_ts = timestamp
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.price_at[self.latest_ts]

    def maximum(self) -> int:
        while True:
            price, ts = self.max_heap[0]
            price = -price
            if self.price_at[ts] == price:
                return price
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while True:
            price, ts = self.min_heap[0]
            if self.price_at[ts] == price:
                return price
            heapq.heappop(self.min_heap)
