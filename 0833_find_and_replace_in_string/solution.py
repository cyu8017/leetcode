# LeetCode 0833 - Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(
        self, s: str, indices: list[int], sources: list[str], targets: list[str]
    ) -> str:
        replace = {}
        for i, src, tgt in zip(indices, sources, targets):
            if s.startswith(src, i):
                replace[i] = (len(src), tgt)
        out = []
        i = 0
        while i < len(s):
            if i in replace:
                length, tgt = replace[i]
                out.append(tgt)
                i += length
            else:
                out.append(s[i])
                i += 1
        return "".join(out)
