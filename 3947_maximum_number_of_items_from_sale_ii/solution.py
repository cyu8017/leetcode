# LeetCode 3947 - Maximum Number of Items From Sale II
# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

from typing import List


class Solution:
    def maxItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        frequency = [0] * (n + 1)
        minimum_price = items[0][1]
        for item in items:
            frequency[item[0]] += 1
            minimum_price = min(minimum_price, item[1])
        batches = []
        for item in items:
            gain = 0
            multiple = item[0]
            while multiple <= n:
                gain += frequency[multiple]
                multiple += item[0]
            gain -= 1
            if gain > 0 and item[1] < 2 * minimum_price:
                batches.append([item[1], gain])
        batches.sort(key=lambda a: a[0])
        remaining = budget
        answer = budget // minimum_price
        boosted = 0
        for current in batches:
            count = current[1]
            affordable = remaining // current[0]
            if affordable < count:
                count = affordable
            remaining -= count * current[0]
            boosted += count
            total = 2 * boosted + remaining // minimum_price
            if total > answer:
                answer = total
            if count < current[1]:
                break
        return answer
