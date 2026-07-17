# LeetCode 1801 - Number of Orders in the Backlog
# https://leetcode.com/problems/number-of-orders-in-the-backlog/

import heapq

MOD = 10**9 + 7


class Solution:
    def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
        buy: list[tuple[int, int]] = []
        sell: list[tuple[int, int]] = []

        for price, amount, order_type in orders:
            if order_type == 0:
                heapq.heappush(buy, (-price, amount))
            else:
                heapq.heappush(sell, (price, amount))

            while buy and sell and -buy[0][0] >= sell[0][0]:
                buy_price, buy_amount = -buy[0][0], buy[0][1]
                sell_price, sell_amount = sell[0]
                matched = min(buy_amount, sell_amount)
                buy_amount -= matched
                sell_amount -= matched
                heapq.heappop(buy)
                heapq.heappop(sell)
                if buy_amount:
                    heapq.heappush(buy, (-buy_price, buy_amount))
                if sell_amount:
                    heapq.heappush(sell, (sell_price, sell_amount))

        total = 0
        for _, amount in buy:
            total = (total + amount) % MOD
        for _, amount in sell:
            total = (total + amount) % MOD
        return total
