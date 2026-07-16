# LeetCode 0911 - Online Election
# https://leetcode.com/problems/online-election/

import bisect


class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        counts: dict[int, int] = {}
        leader = -1
        self.events: list[tuple[int, int]] = []
        for person, time in zip(persons, times):
            counts[person] = counts.get(person, 0) + 1
            if counts[person] >= counts.get(leader, 0):
                leader = person
            self.events.append((time, leader))

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.events, (t, float("inf"))) - 1
        return self.events[i][1]
