from collections import defaultdict
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        pending, answer = defaultdict(list), []
        for person, size in enumerate(groupSizes):
            pending[size].append(person)
            if len(pending[size]) == size:
                answer.append(pending[size])
                pending[size] = []
        return sorted(answer, key=lambda group: (len(group), group))
