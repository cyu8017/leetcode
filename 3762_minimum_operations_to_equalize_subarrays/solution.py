# LeetCode 3762 - Minimum Operations to Equalize Subarrays
# https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

from typing import List, Tuple


class Node:
    def __init__(self, o: "Node" = None):
        if o:
            self.left = o.left
            self.right = o.right
            self.count = o.count
            self.sum = o.sum
        else:
            self.left = 0
            self.right = 0
            self.count = 0
            self.sum = 0


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        quotient = [0] * n
        remainder = [0] * n
        values = [0] * n
        for i in range(n):
            quotient[i] = nums[i] // k
            remainder[i] = nums[i] % k
            values[i] = quotient[i]
        values.sort()
        vu = 1
        for i in range(1, n):
            if values[i] != values[vu - 1]:
                values[vu] = values[i]
                vu += 1
        values = values[:vu]

        nodes = [Node()]
        roots = [0] * (n + 1)
        umax = len(values) - 1

        def lowerBound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def update(previous: int, lo: int, hi: int, position: int, value: int) -> int:
            current = len(nodes)
            nodes.append(Node(nodes[previous]))
            nodes[current].count += 1
            nodes[current].sum += value
            if lo < hi:
                mid = (lo + hi) >> 1
                if position <= mid:
                    nodes[current].left = update(nodes[previous].left, lo, mid, position, value)
                else:
                    nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value)
            return current

        def kth(rightRoot: int, leftRoot: int, lo: int, hi: int, rank: int) -> int:
            if lo == hi:
                return lo
            leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count
            mid = (lo + hi) >> 1
            if rank <= leftCount:
                return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank)
            return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount)

        def prefixStats(rightRoot: int, leftRoot: int, lo: int, hi: int, end: int) -> Tuple[int, int]:
            if end < lo:
                return 0, 0
            if hi <= end:
                return (
                    nodes[rightRoot].count - nodes[leftRoot].count,
                    nodes[rightRoot].sum - nodes[leftRoot].sum,
                )
            mid = (lo + hi) >> 1
            count, total = prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end)
            if end > mid:
                rc, rs = prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end)
                count += rc
                total += rs
            return count, total

        for i in range(n):
            position = lowerBound(values, quotient[i])
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i])

        logv = [0] * (n + 1)
        for i in range(2, n + 1):
            logv[i] = logv[i >> 1] + 1
        levels = logv[n] + 1
        minTable = [None] * levels
        maxTable = [None] * levels
        minTable[0] = remainder[:]
        maxTable[0] = remainder[:]
        for level in range(1, levels):
            length = n - (1 << level) + 1
            minTable[level] = [0] * length
            maxTable[level] = [0] * length
            half = 1 << (level - 1)
            for i in range(length):
                minTable[level][i] = min(minTable[level - 1][i], minTable[level - 1][i + half])
                maxTable[level][i] = max(maxTable[level - 1][i], maxTable[level - 1][i + half])

        answer = [0] * len(queries)
        for qi, (left, right) in enumerate(queries):
            length = right - left + 1
            level = logv[length]
            offset = right - (1 << level) + 1
            minR = min(minTable[level][left], minTable[level][offset])
            maxR = max(maxTable[level][left], maxTable[level][offset])
            if minR != maxR:
                answer[qi] = -1
                continue
            medianIndex = kth(roots[right + 1], roots[left], 0, umax, (length + 1) // 2)
            median = values[medianIndex]
            leftCount, leftSum = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex)
            totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum
            answer[qi] = median * leftCount - leftSum + (totalSum - leftSum) - median * (length - leftCount)
        return answer
