# LeetCode 2884 - Modify Columns
# https://leetcode.com/problems/modify-columns/

from typing import Any, List


class Solution:
    def modifySalaryColumn(self, employees: List[Any]) -> List[Any]:
        out = []
        for r in employees:
            if isinstance(r, list):
                out.append([r[0], r[1] * 2])
            else:
                row = dict(r)
                row["salary"] = r["salary"] * 2
                out.append(row)
        return out
