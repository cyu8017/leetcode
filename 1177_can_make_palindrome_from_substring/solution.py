# LeetCode 1177 - Can Make Palindrome from Substring
# https://leetcode.com/problems/can-make-palindrome-from-substring/

class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        prefix = [0]
        mask = 0
        for ch in s:
            mask ^= 1 << (ord(ch) - 97)
            prefix.append(mask)
        ans = []
        for left, right, k in queries:
            bits = (prefix[right + 1] ^ prefix[left]).bit_count()
            ans.append(bits // 2 <= k)
        return ans
