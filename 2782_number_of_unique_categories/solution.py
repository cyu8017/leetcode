# LeetCode 2782 - Number of Unique Categories
# https://leetcode.com/problems/number-of-unique-categories/


class Solution:
    def numberOfCategories(self, n: int, categoryHandler) -> int:
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(i + 1, n):
                if categoryHandler.haveSameCategory(i, j):
                    a, b = find(i), find(j)
                    if a != b:
                        parent[a] = b
        return sum(1 for i in range(n) if find(i) == i)
