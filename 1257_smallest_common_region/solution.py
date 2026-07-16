from typing import List

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for group in regions:
            for child in group[1:]:
                parent[child] = group[0]
        ancestors = set()
        while region1:
            ancestors.add(region1)
            region1 = parent.get(region1)
        while region2 not in ancestors:
            region2 = parent[region2]
        return region2
