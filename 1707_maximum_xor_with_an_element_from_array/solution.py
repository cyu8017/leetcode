from typing import List


class Trie:
    def __init__(self) -> None:
        self.child = [None, None]


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        indexed = sorted((m, x, i) for i, (x, m) in enumerate(queries))
        ans = [-1] * len(queries)
        root = Trie()
        added = 0

        def insert(num: int) -> None:
            node = root
            for bit in range(31, -1, -1):
                b = (num >> bit) & 1
                if node.child[b] is None:
                    node.child[b] = Trie()
                node = node.child[b]

        for limit, x, qi in indexed:
            while added < len(nums) and nums[added] <= limit:
                insert(nums[added])
                added += 1
            if added == 0:
                continue
            node = root
            value = 0
            for bit in range(31, -1, -1):
                b = (x >> bit) & 1
                want = b ^ 1
                if node.child[want] is not None:
                    value |= 1 << bit
                    node = node.child[want]
                else:
                    node = node.child[b]
            ans[qi] = value
        return ans
