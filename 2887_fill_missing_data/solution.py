# LeetCode 2887 - Fill Missing Data
# https://leetcode.com/problems/fill-missing-data/

from typing import Any, List


class Solution:
    def fillMissingValues(self, products: List[Any]) -> List[Any]:
        out = []
        for r in products:
            if isinstance(r, list):
                q = r[1]
                out.append([r[0], 0 if q is None else q, r[2]])
            else:
                row = dict(r)
                row["quantity"] = 0 if r.get("quantity") is None else r["quantity"]
                out.append(row)
        return out
