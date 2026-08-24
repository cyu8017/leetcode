# LeetCode 3799 - Word Squares II
# https://leetcode.com/problems/word-squares-ii/

from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        words = sorted(words)
        n = len(words)
        ans = []
        for i in range(n):
            top = words[i]
            for j in range(n):
                if j == i:
                    continue
                left = words[j]
                for k in range(n):
                    if k == j or k == i:
                        continue
                    right = words[k]
                    for h in range(n):
                        if h == k or h == j or h == i:
                            continue
                        bottom = words[h]
                        if (top[0] == left[0] and top[3] == right[0] and
                                bottom[0] == left[3] and bottom[3] == right[3]):
                            ans.append([top, left, right, bottom])
        return ans
