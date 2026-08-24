# LeetCode 2890 - Reshape Data: Melt
# https://leetcode.com/problems/reshape-data-melt/

from typing import Any, List


class Solution:
    def meltTable(self, report: List[Any]) -> List[Any]:
        out = []
        for r in report:
            if isinstance(r, list):
                product = r[0]
                for q in range(1, 5):
                    out.append({"product": product, "quarter": "quarter_" + str(q), "sales": r[q]})
            else:
                for q in ["quarter_1", "quarter_2", "quarter_3", "quarter_4"]:
                    out.append({"product": r["product"], "quarter": q, "sales": r[q]})
        return out
