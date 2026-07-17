# LeetCode 1813 - Sentence Similarity III
# https://leetcode.com/problems/sentence-similarity-iii/


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        n1, n2 = len(words1), len(words2)

        i = 0
        while i < n1 and i < n2 and words1[i] == words2[i]:
            i += 1
        if i == n1 or i == n2:
            return True

        j1, j2 = n1 - 1, n2 - 1
        while j1 >= i and j2 >= i and words1[j1] == words2[j2]:
            j1 -= 1
            j2 -= 1
        return j1 < i or j2 < i
