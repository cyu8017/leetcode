# LeetCode 1505

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)
    def add(self, i, delta):
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i
    def sum(self, i):
        out = 0
        while i:
            out += self.bit[i]
            i -= i & -i
        return out

class Solution:
    def minInteger(self, num, k):
        from collections import deque
        positions = [deque() for _ in range(10)]
        for i, ch in enumerate(num):
            positions[int(ch)].append(i)
        fw = Fenwick(len(num))
        out = []
        for _ in num:
            for digit in range(10):
                if not positions[digit]:
                    continue
                index = positions[digit][0]
                cost = index - fw.sum(index)
                if cost <= k:
                    k -= cost
                    positions[digit].popleft()
                    fw.add(index, 1)
                    out.append(str(digit))
                    break
        return "".join(out)
