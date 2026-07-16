from collections import deque

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list[int]:
        answer = [0] if low == 0 else []
        q = deque(range(1, 10))
        while q:
            x = q.popleft()
            if x > high: continue
            if x >= low: answer.append(x)
            last = x % 10
            if last > 0: q.append(x * 10 + last - 1)
            if last < 9: q.append(x * 10 + last + 1)
        return sorted(answer)
