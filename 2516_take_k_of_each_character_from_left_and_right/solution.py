# LeetCode 2516 - Take K of Each Character From Left and Right
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        cnt = [0, 0, 0]
        for c in s:
            cnt[ord(c) - 97] += 1
        if cnt[0] < k or cnt[1] < k or cnt[2] < k:
            return -1
        need = [cnt[0] - k, cnt[1] - k, cnt[2] - k]
        window = [0, 0, 0]
        left = 0
        max_mid = 0
        for right in range(n):
            window[ord(s[right]) - 97] += 1
            while window[0] > need[0] or window[1] > need[1] or window[2] > need[2]:
                window[ord(s[left]) - 97] -= 1
                left += 1
            if right - left + 1 > max_mid:
                max_mid = right - left + 1
        return n - max_mid
