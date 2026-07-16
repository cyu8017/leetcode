# LeetCode 0818 - Race Car
# https://leetcode.com/problems/race-car/

from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # position, speed, steps
        seen = {(0, 1)}
        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            nxt_pos, nxt_speed = pos + speed, speed * 2
            if (nxt_pos, nxt_speed) not in seen and abs(nxt_pos) < target * 2:
                seen.add((nxt_pos, nxt_speed))
                queue.append((nxt_pos, nxt_speed, steps + 1))
            rev_speed = -1 if speed > 0 else 1
            if (pos, rev_speed) not in seen:
                seen.add((pos, rev_speed))
                queue.append((pos, rev_speed, steps + 1))
        return -1
