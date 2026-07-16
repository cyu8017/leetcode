# LeetCode 0358 - Rearrange String k Distance Apart
# https://leetcode.com/problems/rearrange-string-k-distance-apart/

import heapq
from collections import Counter, deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        max_freq_chars = sum(1 for count in counts.values() if count == max_freq)

        if (len(s) - max_freq_chars) < (max_freq - 1) * (k - 1):
            return ""

        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)
        queue: deque[tuple[int, str, int]] = deque()
        result: list[str] = []
        index = 0

        while heap or queue:
            while queue and queue[0][2] <= index:
                count, char, _ = queue.popleft()
                heapq.heappush(heap, (count, char))

            if not heap:
                return ""

            count, char = heapq.heappop(heap)
            result.append(char)
            if count + 1 < 0:
                queue.append((count + 1, char, index + k))
            index += 1

        return "".join(result)
