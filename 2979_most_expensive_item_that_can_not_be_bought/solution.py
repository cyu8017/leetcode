# LeetCode 2979 - Most Expensive Item That Can Not Be Bought
# https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/


class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        return primeOne * primeTwo - primeOne - primeTwo
