# LeetCode 3823 - Reverse Letters Then Special Characters in a String
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution:
    def reverseByType(self, s: str) -> str:
        a = []
        b = []
        for c in s:
            if ("A" <= c <= "Z") or ("a" <= c <= "z"):
                a.append(c)
            else:
                b.append(c)
        j = len(a)
        k = len(b)
        arr = list(s)
        for i in range(len(arr)):
            if ("A" <= arr[i] <= "Z") or ("a" <= arr[i] <= "z"):
                j -= 1
                arr[i] = a[j]
            else:
                k -= 1
                arr[i] = b[k]
        return "".join(arr)
