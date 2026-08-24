# LeetCode 2880 - Select Data
# https://leetcode.com/problems/select-data/

from typing import Any, List


class Solution:
    def selectData(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            if (r[0] if isinstance(r, list) else r.get("student_id")) == 101:
                if isinstance(r, list):
                    out.append({"name": r[1], "age": r[2]})
                else:
                    out.append({"name": r["name"], "age": r["age"]})
        return out
