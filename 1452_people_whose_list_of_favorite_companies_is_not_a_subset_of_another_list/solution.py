from typing import List, Optional

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(x) for x in favoriteCompanies]
        return [i for i, s in enumerate(sets)
                if not any(i != j and s <= t for j, t in enumerate(sets))]
