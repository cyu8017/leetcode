# LeetCode 0850 - Rectangle Area II
# https://leetcode.com/problems/rectangle-area-ii/

class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 10**9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
        events.sort()

        def covered_length(active: list[tuple[int, int]]) -> int:
            if not active:
                return 0
            active.sort()
            total = 0
            cur_start, cur_end = active[0]
            for start, end in active[1:]:
                if start > cur_end:
                    total += cur_end - cur_start
                    cur_start, cur_end = start, end
                else:
                    cur_end = max(cur_end, end)
            total += cur_end - cur_start
            return total

        active: list[tuple[int, int]] = []
        area = 0
        prev_x = events[0][0]
        for x, typ, y1, y2 in events:
            area += covered_length(active) * (x - prev_x)
            if typ == 1:
                active.append((y1, y2))
            else:
                active.remove((y1, y2))
            prev_x = x
        return area % MOD
