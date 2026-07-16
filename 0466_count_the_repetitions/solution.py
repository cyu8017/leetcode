# LeetCode 0466 - Count The Repetitions
# https://leetcode.com/problems/count-the-repetitions/


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not s2:
            return 0

        index = 0
        s2_count = 0
        record: dict[int, tuple[int, int]] = {}

        for repeat in range(n1):
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        s2_count += 1
            if index in record:
                previous_repeat, previous_count = record[index]
                cycle = repeat - previous_repeat
                count_cycle = s2_count - previous_count
                remaining = n1 - repeat - 1
                s2_count += (remaining // cycle) * count_cycle
                repeat += (remaining // cycle) * cycle
                if repeat >= n1 - 1:
                    break
                previous_repeat, previous_count = record[index]
            record[index] = (repeat, s2_count)

        return s2_count // n2
