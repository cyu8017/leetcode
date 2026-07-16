class Solution:
    def findLexSmallestString(self, s, a, b):
        seen = {s}; q = [s]; ans = s
        for cur in q:
            ans = min(ans, cur)
            add = "".join(str((int(ch) + (a if i % 2 else 0)) % 10) for i, ch in enumerate(cur))
            rot = cur[-b:] + cur[:-b]
            for nxt in (add, rot):
                if nxt not in seen: seen.add(nxt); q.append(nxt)
        return ans
