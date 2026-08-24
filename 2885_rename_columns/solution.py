# LeetCode 2885 - Rename Columns
# https://leetcode.com/problems/rename-columns/

from typing import Any, List


class Solution:
    def renameColumns(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            if isinstance(r, list):
                out.append(
                    {
                        "student_id": r[0],
                        "first_name": r[1],
                        "last_name": r[2],
                        "age_in_years": r[3],
                    }
                )
            else:
                out.append(
                    {
                        "student_id": r["id"],
                        "first_name": r["first"],
                        "last_name": r["last"],
                        "age_in_years": r["age"],
                    }
                )
        return out
