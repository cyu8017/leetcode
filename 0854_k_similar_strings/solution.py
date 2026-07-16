# LeetCode 0854 - K-Similar Strings
# https://leetcode.com/problems/k-similar-strings/

from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        s1 = list(s1)
        target = s2
        s1_str = "".join(s1)
        queue = deque([(s1_str, 0)])
        seen = {s1_str}

        def neighbors(s: str) -> list[str]:
            arr = list(s)
            i = 0
            while arr[i] == target[i]:
                i += 1
            res = []
            for j in range(i + 1, len(arr)):
                if arr[j] == target[i] and arr[j] != target[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    res.append("".join(arr))
                    arr[i], arr[j] = arr[j], arr[i]
            return res

        while queue:
            cur, dist = queue.popleft()
            for nxt in neighbors(cur):
                if nxt == target:
                    return dist + 1
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, dist + 1))
        return -1
