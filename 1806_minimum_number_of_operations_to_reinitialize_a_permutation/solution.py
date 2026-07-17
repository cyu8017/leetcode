# LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        target = perm[:]
        operations = 0

        while True:
            new_perm = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new_perm[i] = perm[i // 2]
                else:
                    new_perm[i] = perm[n // 2 + (i - 1) // 2]
            perm = new_perm
            operations += 1
            if perm == target:
                return operations
