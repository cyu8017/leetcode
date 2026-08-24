# LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
# https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        stk = []
        for c in s:
            while (stk and stk[-1] > c and cnt[ord(stk[-1]) - 97] > 1):
                cnt[ord(stk[-1]) - 97] -= 1
                stk.pop()
            stk.append(c)
        while cnt[ord(stk[-1]) - 97] > 1:
            cnt[ord(stk[-1]) - 97] -= 1
            stk.pop()
        return "".join(stk)
