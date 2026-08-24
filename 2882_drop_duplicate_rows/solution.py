# LeetCode 2882 - Drop Duplicate Rows
# https://leetcode.com/problems/drop-duplicate-rows/

from typing import Any, List


class Solution:
    def dropDuplicateEmails(self, customers: List[Any]) -> List[Any]:
        seen = set()
        out = []
        for r in customers:
            email = r[2] if isinstance(r, list) else r["email"]
            if email in seen:
                continue
            seen.add(email)
            out.append(r)
        return out
