# LeetCode 2886 - Change Data Type
# https://leetcode.com/problems/change-data-type/

from typing import Any, List


class Solution:
    def changeDatatype(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            if isinstance(r, list):
                out.append([r[0], r[1], r[2], int(r[3])])
            else:
                row = dict(r)
                row["grade"] = int(r["grade"])
                out.append(row)
        return out
