# LeetCode 2883 - Drop Missing Data
# https://leetcode.com/problems/drop-missing-data/

from typing import Any, List


class Solution:
    def dropMissingData(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            name = r[1] if isinstance(r, list) else r.get("name")
            if name is not None and name != "":
                out.append(r)
        return out
