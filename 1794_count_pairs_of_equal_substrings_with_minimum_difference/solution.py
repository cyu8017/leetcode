class Solution:
    def countQuadruples(self, firstString, secondString):
        first = {}
        last_f = {}
        last_s = {}
        for i, ch in enumerate(firstString):
            if ch not in first:
                first[ch] = i
            last_f[ch] = i
        for i, ch in enumerate(secondString):
            last_s[ch] = i
        best = float("inf")
        for ch in first:
            if ch in last_s:
                best = min(best, last_f[ch] - last_s[ch])
        if best == float("inf"):
            return 0
        ans = 0
        for ch in first:
            if ch not in last_s or last_f[ch] - last_s[ch] != best:
                continue
            i_count = sum(1 for k in range(first[ch], last_f[ch] + 1) if firstString[k] == ch)
            a_count = sum(1 for k in range(0, last_s[ch] + 1) if secondString[k] == ch)
            ans += i_count * a_count
        return ans
