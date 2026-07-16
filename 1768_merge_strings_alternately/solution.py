class Solution:
    def mergeAlternately(self, word1, word2):
        i = j = 0
        out = []
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                out.append(word1[i]); i += 1
            if j < len(word2):
                out.append(word2[j]); j += 1
        return "".join(out)
