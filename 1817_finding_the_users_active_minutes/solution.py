# LeetCode 1817 - Finding the Users Active Minutes
# https://leetcode.com/problems/finding-the-users-active-minutes/

from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes: dict[int, set[int]] = defaultdict(set)
        for user_id, minute in logs:
            user_minutes[user_id].add(minute)

        answer = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            if uam <= k:
                answer[uam - 1] += 1
        return answer
