# LeetCode 3943 - Number of Pairs After Increment
# https://leetcode.com/problems/number-of-pairs-after-increment/

from typing import Dict, List


def rebuild(freq: List[Dict[int, int]], nums2: List[int], b: int, blockSize: int, n: int) -> None:
    freq[b].clear()
    end = min((b + 1) * blockSize, n)
    for i in range(b * blockSize, end):
        freq[b][nums2[i]] = freq[b].get(nums2[i], 0) + 1


def push(lazy: List[int], nums2: List[int], b: int, blockSize: int, n: int) -> None:
    if lazy[b] != 0:
        end = min((b + 1) * blockSize, n)
        for i in range(b * blockSize, end):
            nums2[i] += lazy[b]
        lazy[b] = 0


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        block_size = 225
        n = len(nums2)
        blocks = (n + block_size - 1) // block_size
        lazy = [0] * blocks
        freq: List[Dict[int, int]] = [{} for _ in range(blocks)]
        for b in range(blocks):
            rebuild(freq, nums2, b, block_size, n)
        fixed: Dict[int, int] = {}
        for x in nums1:
            fixed[x] = fixed.get(x, 0) + 1
        answer: List[int] = []
        for q in queries:
            if q[0] == 1:
                l, r, delta = q[1], q[2], q[3]
                first = l // block_size
                last = r // block_size
                if first == last:
                    push(lazy, nums2, first, block_size, n)
                    for i in range(l, r + 1):
                        nums2[i] += delta
                    rebuild(freq, nums2, first, block_size, n)
                    continue
                push(lazy, nums2, first, block_size, n)
                for i in range(l, (first + 1) * block_size):
                    nums2[i] += delta
                rebuild(freq, nums2, first, block_size, n)
                push(lazy, nums2, last, block_size, n)
                for i in range(last * block_size, r + 1):
                    nums2[i] += delta
                rebuild(freq, nums2, last, block_size, n)
                for b in range(first + 1, last):
                    lazy[b] += delta
            else:
                total = 0
                for a, count_a in fixed.items():
                    target = q[1] - a
                    for b in range(blocks):
                        c = freq[b].get(target - lazy[b])
                        if c is not None:
                            total += count_a * c
                answer.append(total)
        return answer
