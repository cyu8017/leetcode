# LeetCode 2881 - Create a New Column
# https://leetcode.com/problems/create-a-new-column/

from typing import Any, List


class Solution:
    def createBonusColumn(self, employees: List[Any]) -> List[Any]:
        out = []
        for r in employees:
            if isinstance(r, list):
                out.append({"name": r[0], "salary": r[1], "bonus": r[1] * 2})
            else:
                row = dict(r)
                row["bonus"] = r["salary"] * 2
                out.append(row)
        return out
