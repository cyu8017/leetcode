class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            start, end = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
            if end - start >= duration: return [start, start + duration]
            if slots1[i][1] < slots2[j][1]: i += 1
            else: j += 1
        return []
