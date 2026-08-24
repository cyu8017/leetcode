# LeetCode 2866 - Beautiful Towers II
# https://leetcode.com/problems/beautiful-towers-ii/

from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left = [0] * n
        st = [-1]
        s = 0
        for i in range(n):
            while len(st) > 1 and maxHeights[st[-1]] >= maxHeights[i]:
                j = st.pop()
                s -= maxHeights[j] * (j - st[-1])
            s += maxHeights[i] * (i - st[-1])
            left[i] = s
            st.append(i)
        right = [0] * n
        st = [n]
        s = 0
        for i in range(n - 1, -1, -1):
            while len(st) > 1 and maxHeights[st[-1]] >= maxHeights[i]:
                j = st.pop()
                s -= maxHeights[j] * (st[-1] - j)
            s += maxHeights[i] * (st[-1] - i)
            right[i] = s
            st.append(i)
        ans = 0
        for i in range(n):
            cand = left[i] + right[i] - maxHeights[i]
            if cand > ans:
                ans = cand
        return ans
