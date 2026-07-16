from typing import List, Optional

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        reach = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            reach[a][b] = True
        for k in range(numCourses):
            for i in range(numCourses):
                if reach[i][k]:
                    for j in range(numCourses):
                        reach[i][j] |= reach[k][j]
        return [reach[a][b] for a, b in queries]
