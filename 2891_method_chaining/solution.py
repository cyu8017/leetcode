# LeetCode 2891 - Method Chaining
# https://leetcode.com/problems/method-chaining/

from typing import Any, List


class Solution:
    def findHeavyAnimals(self, animals: List[Any]) -> List[Any]:
        def weight(r: Any) -> int:
            return r[3] if isinstance(r, list) else r["weight"]

        filtered = [r for r in animals if weight(r) > 100]
        filtered.sort(key=weight, reverse=True)
        return [{"name": r[0] if isinstance(r, list) else r["name"]} for r in filtered]
