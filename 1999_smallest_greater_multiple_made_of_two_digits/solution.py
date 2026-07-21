from collections import deque

class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        digits = sorted({digit1, digit2})
        q = deque()
        for d in digits:
            if d != 0:
                q.append(d)
        if not q:
            return -1
        seen = set(q)
        while q:
            x = q.popleft()
            if x > k and x % k == 0:
                return x
            for d in digits:
                nx = x * 10 + d
                if nx <= 2**31 - 1 and nx not in seen:
                    seen.add(nx)
                    q.append(nx)
        return -1
