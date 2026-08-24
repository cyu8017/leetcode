# LeetCode 3406 - Find the Lexicographically Largest String From the Box II
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_len = n - (numFriends - 1)
        ans = ""
        for i in range(n):
            end = i + max_len
            if end > n:
                end = n
            cand = word[i:end]
            if cand > ans:
                ans = cand
        return ans
