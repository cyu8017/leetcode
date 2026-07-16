# LeetCode 0406 - Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (-person[0], person[1]))
        queue: list[list[int]] = []
        for person in people:
            queue.insert(person[1], person)
        return queue
