class Solution:
    def largestMerge(self, word1, word2):
        i = j = 0
        out = []
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                out.append(word1[i]); i += 1
            else:
                out.append(word2[j]); j += 1
        out.extend(word1[i:]); out.extend(word2[j:])
        return "".join(out)
