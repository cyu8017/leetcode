# LeetCode 3606 - Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator/

from typing import List


def check3606(s: str) -> bool:
    if not s:
        return False
    for c in s:
        if not (c.isalnum() or c == "_"):
            return False
    return True


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        bs = {"electronics", "grocery", "pharmacy", "restaurant"}
        idx = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in bs and check3606(code[i]):
                idx.append(i)
        idx.sort(key=lambda i: (businessLine[i], code[i]))
        return [code[i] for i in idx]
