# LeetCode 3458 - Select K Disjoint Special Substrings
# https://leetcode.com/problems/select-k-disjoint-special-substrings/


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            ci = ord(ch) - 97
            if first[ci] == n:
                first[ci] = i
            last[ci] = i
        segs = []
        for c in range(26):
            if last[c] == -1:
                continue
            l, r = first[c], last[c]
            i = l
            while i <= r:
                ci = ord(s[i]) - 97
                if first[ci] < l:
                    l = first[ci]
                    i = l - 1
                    i += 1
                    continue
                if last[ci] > r:
                    r = last[ci]
                i += 1
            if not (l == 0 and r == n - 1):
                segs.append((l, r))
        uniq = set()
        arr = []
        for sg in segs:
            key = (sg[0] << 32) | (sg[1] & 0xFFFFFFFF)
            if key not in uniq:
                uniq.add(key)
                arr.append(sg)
        arr.sort(key=lambda x: x[1])
        cnt, end = 0, -1
        for sg in arr:
            if sg[0] > end:
                cnt += 1
                end = sg[1]
        return cnt >= k
