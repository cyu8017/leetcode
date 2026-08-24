# LeetCode 3845 - Maximum Subarray XOR with Bounded Range
# https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

from typing import List


class Solution:
    def maxSubarrayXor(self, nums: List[int], k: int) -> int:
        nodes = [{"next": [0, 0], "count": 0}]

        def add(x: int, delta: int) -> None:
            u = 0
            nodes[u]["count"] += delta
            for b in range(15, -1, -1):
                bit = (x >> b) & 1
                if nodes[u]["next"][bit] == 0:
                    nodes[u]["next"][bit] = len(nodes)
                    nodes.append({"next": [0, 0], "count": 0})
                u = nodes[u]["next"][bit]
                nodes[u]["count"] += delta

        def query(x: int) -> int:
            u = 0
            res = 0
            for b in range(15, -1, -1):
                bit = (x >> b) & 1
                want = bit ^ 1
                v = nodes[u]["next"][want]
                if v != 0 and nodes[v]["count"] > 0:
                    res |= 1 << b
                    u = v
                else:
                    u = nodes[u]["next"][bit]
            return res

        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]
        max_q: List[int] = []
        min_q: List[int] = []
        left = 0
        trie_left = 0
        ans = 0
        for r in range(n):
            x = nums[r]
            while max_q and nums[max_q[-1]] <= x:
                max_q.pop()
            max_q.append(r)
            while min_q and nums[min_q[-1]] >= x:
                min_q.pop()
            min_q.append(r)
            while nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == left:
                    max_q.pop(0)
                if min_q[0] == left:
                    min_q.pop(0)
                left += 1
            add(pref[r], 1)
            while trie_left < left:
                add(pref[trie_left], -1)
                trie_left += 1
            cur = query(pref[r + 1])
            if cur > ans:
                ans = cur
        return ans
