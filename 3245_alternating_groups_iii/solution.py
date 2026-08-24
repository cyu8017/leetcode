# LeetCode 3245 - Alternating Groups III
# https://leetcode.com/problems/alternating-groups-iii/

from typing import List, Set


class SegTree:
    def __init__(self, n_: int):
        self.n = n_
        self.treeIntervalCounts = [0] * (4 * n_)
        self.treeIntervalLengths = [0] * (4 * n_)

    def add(self, i: int, val: int) -> None:
        self.addRec(0, 0, self.n - 1, i, val)

    def addRec(self, treeIndex: int, lo: int, hi: int, i: int, val: int) -> None:
        if lo == hi:
            self.treeIntervalCounts[treeIndex] += val
            self.treeIntervalLengths[treeIndex] = self.treeIntervalCounts[treeIndex] * i
            return
        mid = (lo + hi) >> 1
        if i <= mid:
            self.addRec(2 * treeIndex + 1, lo, mid, i, val)
        else:
            self.addRec(2 * treeIndex + 2, mid + 1, hi, i, val)
        self.treeIntervalCounts[treeIndex] = (
            self.treeIntervalCounts[2 * treeIndex + 1] + self.treeIntervalCounts[2 * treeIndex + 2]
        )
        self.treeIntervalLengths[treeIndex] = (
            self.treeIntervalLengths[2 * treeIndex + 1] + self.treeIntervalLengths[2 * treeIndex + 2]
        )

    def queryIntervalCounts(self, i: int) -> int:
        return self.query(self.treeIntervalCounts, 0, 0, self.n - 1, i, self.n - 1)

    def queryIntervalLengths(self, i: int) -> int:
        return self.query(self.treeIntervalLengths, 0, 0, self.n - 1, i, self.n - 1)

    def query(self, tree: List[int], treeIndex: int, lo: int, hi: int, i: int, j: int) -> int:
        if i <= lo and hi <= j:
            return tree[treeIndex]
        if j < lo or hi < i:
            return 0
        mid = (lo + hi) >> 1
        return self.query(tree, treeIndex * 2 + 1, lo, mid, i, j) + self.query(
            tree, treeIndex * 2 + 2, mid + 1, hi, i, j
        )


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        ans = []
        arr = [0] * (2 * n - 1)
        for i in range(n):
            arr[i] = colors[i]
        for i in range(n - 1):
            arr[n + i] = colors[i]

        def pack(l: int, r: int) -> int:
            return (l << 32) | (r & 0xFFFFFFFF)

        def unpackL(v: int) -> int:
            return v >> 32

        def unpackR(v: int) -> int:
            return v & 0xFFFFFFFF

        tree = SegTree(2 * n - 1)
        intervals: Set[int] = set()

        def insert(l: int, r: int) -> None:
            intervals.add(pack(l, r))
            if l < n:
                tree.add(r - l + 1, 1)

        def remove(l: int, r: int) -> None:
            intervals.discard(pack(l, r))
            if l < n:
                tree.add(r - l + 1, -1)

        def findInterval(target: int) -> List[int]:
            bestL, bestR = -1, -1
            for k in intervals:
                kl, kr = unpackL(k), unpackR(k)
                if kl <= target <= kr and kl > bestL:
                    bestL, bestR = kl, kr
            return [bestL, bestR]

        def getNum(sz: int) -> int:
            numIntervals = tree.queryIntervalCounts(sz)
            sumIntervals = tree.queryIntervalLengths(sz)
            numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals
            l, r = findInterval(n)
            if l < 0 or l >= n or r - l + 1 < sz:
                return numAlternatingGroups
            if r >= n:
                nonDuplicateGroups = n - l
                numGroups = (r - l + 1) - sz + 1
                extra = numGroups - nonDuplicateGroups
                if extra > 0:
                    numAlternatingGroups -= extra
            return numAlternatingGroups

        def update(index: int, color: int) -> None:
            if arr[index] == color:
                return
            arr[index] = color
            start, end = findInterval(index)
            remove(start, end)
            if start < index < end:
                insert(start, index - 1)
                insert(index, index)
                insert(index + 1, end)
                return
            if start == index and index < end:
                insert(start + 1, end)
            if start < index and index == end:
                insert(start, end - 1)
            ns, ne = index, index
            while True:
                merged = False
                for k in list(intervals):
                    kl, kr = unpackL(k), unpackR(k)
                    if kr + 1 == ns and arr[kr] != arr[ns]:
                        remove(kl, kr)
                        ns = kl
                        merged = True
                        break
                if not merged:
                    break
            while True:
                merged = False
                for k in list(intervals):
                    kl, kr = unpackL(k), unpackR(k)
                    if kl == ne + 1 and arr[kl] != arr[ne]:
                        remove(kl, kr)
                        ne = kr
                        merged = True
                        break
                if not merged:
                    break
            insert(ns, ne)

        st = 0
        for i in range(1, 2 * n - 1):
            if arr[i] == arr[i - 1]:
                insert(st, i - 1)
                st = i
        insert(st, 2 * n - 2)
        for query in queries:
            if query[0] == 1:
                ans.append(getNum(query[1]))
            else:
                index, color = query[1], query[2]
                if arr[index] != color:
                    update(index, color)
                    if index < n - 1:
                        update(index + n, color)
        return ans
