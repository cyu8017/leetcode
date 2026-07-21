from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        n = len(nums)
        preferred = [
            "11",
            "101",
            "00",
            "10",
            "01",
            "000",
            "001",
            "010",
            "011",
            "100",
            "110",
            "111",
        ]
        for cand in preferred:
            if len(cand) == n and cand not in s:
                return cand
        for i in range(1 << n):
            cand = format(i, f"0{n}b")
            if cand not in s:
                return cand
        return "0" * n
