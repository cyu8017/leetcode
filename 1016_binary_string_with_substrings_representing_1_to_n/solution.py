# LeetCode 1016 - Binary String With Substrings Representing 1 To N
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(i)[2:] in s for i in range(n, n // 2, -1))
