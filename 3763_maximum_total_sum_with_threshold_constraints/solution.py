# LeetCode 3763 - Maximum Total Sum with Threshold Constraints
# https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], threshold: List[int]) -> int:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: threshold[i])
        tree = []

        def push(x: int) -> None:
            tree.append(x)
            i = len(tree) - 1
            while i > 0:
                p = (i - 1) >> 1
                if tree[i] <= tree[p]:
                    break
                tree[i], tree[p] = tree[p], tree[i]
                i = p

        def pop() -> int:
            top = tree[0]
            last = tree.pop()
            if tree:
                tree[0] = last
                i = 0
                while True:
                    s = i
                    l = i * 2 + 1
                    r = l + 1
                    if l < len(tree) and tree[l] > tree[s]:
                        s = l
                    if r < len(tree) and tree[r] > tree[s]:
                        s = r
                    if s == i:
                        break
                    tree[i], tree[s] = tree[s], tree[i]
                    i = s
            return top

        ans = 0
        i = 0
        step = 1
        while True:
            while i < n and threshold[idx[i]] <= step:
                push(nums[idx[i]])
                i += 1
            if not tree:
                break
            ans += pop()
            step += 1
        return ans
