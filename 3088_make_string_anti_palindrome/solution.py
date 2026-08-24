# LeetCode 3088 - Make String Anti-palindrome
# https://leetcode.com/problems/make-string-anti-palindrome/


class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        arr = sorted(s)
        n = len(arr)
        m = n // 2
        if arr[m] == arr[m - 1]:
            i = m
            while i < n and arr[i] == arr[i - 1]:
                i += 1
            j = m
            while j < n and arr[j] == arr[n - j - 1]:
                if i >= n:
                    return "-1"
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
        return "".join(arr)
