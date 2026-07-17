# LeetCode 1868 - Product of Two Run-Length Encoded Arrays
# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

from typing import List


class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        result: List[List[int]] = []
        i = j = 0
        rem1 = encoded1[0][1]
        rem2 = encoded2[0][1]

        while i < len(encoded1):
            take = min(rem1, rem2)
            value = encoded1[i][0] * encoded2[j][0]
            if result and result[-1][0] == value:
                result[-1][1] += take
            else:
                result.append([value, take])

            rem1 -= take
            rem2 -= take
            if rem1 == 0:
                i += 1
                if i < len(encoded1):
                    rem1 = encoded1[i][1]
            if rem2 == 0:
                j += 1
                if j < len(encoded2):
                    rem2 = encoded2[j][1]

        return result
