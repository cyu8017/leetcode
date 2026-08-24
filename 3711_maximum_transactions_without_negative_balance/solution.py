# LeetCode 3711 - Maximum Transactions Without Negative Balance
# https://leetcode.com/problems/maximum-transactions-without-negative-balance/

from typing import List
import heapq


class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        tm = {}
        ans = len(transactions)
        s = 0
        heap = []

        for x in transactions:
            s += x
            tm[x] = tm.get(x, 0) + 1
            heapq.heappush(heap, x)
            while s < 0:
                while heap and tm.get(heap[0], 0) == 0:
                    heapq.heappop(heap)
                y = heap[0]
                s -= y
                ans -= 1
                c = tm[y]
                if c == 1:
                    del tm[y]
                    heapq.heappop(heap)
                else:
                    tm[y] = c - 1
                    heapq.heappop(heap)
        return ans
