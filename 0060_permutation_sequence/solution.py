# LeetCode 0060 - Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        factorials = [1] * n

        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i

        k -= 1
        result: list[str] = []

        for i in range(n - 1, -1, -1):
            index = k // factorials[i]
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= factorials[i]

        return "".join(result)
