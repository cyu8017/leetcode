from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        max_def = 0
        for i in range(len(properties) - 1, -1, -1):
            if properties[i][1] < max_def:
                ans += 1
            else:
                max_def = properties[i][1]
        return ans
