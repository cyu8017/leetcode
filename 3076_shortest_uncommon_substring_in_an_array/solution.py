# LeetCode 3076 - Shortest Uncommon Substring in an Array
# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        ans = [""] * n
        for i in range(n):
            s = arr[i]
            m = len(s)
            j = 1
            while j <= m and ans[i] == "":
                for l in range(0, m - j + 1):
                    sub = s[l : l + j]
                    if ans[i] == "" or ans[i] > sub:
                        ok = True
                        for k in range(n):
                            if k != i and sub in arr[k]:
                                ok = False
                                break
                        if ok:
                            ans[i] = sub
                j += 1
        return ans
