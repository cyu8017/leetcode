# LeetCode 3083 - Existence of a Substring in a String and Its Reverse
# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        st = [[False] * 26 for _ in range(26)]
        for i in range(len(s) - 1):
            st[ord(s[i + 1]) - 97][ord(s[i]) - 97] = True
        for i in range(len(s) - 1):
            if st[ord(s[i]) - 97][ord(s[i + 1]) - 97]:
                return True
        return False
