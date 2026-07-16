from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = {v for _, v in edges}
        return [v for v in range(n) if v not in incoming]
