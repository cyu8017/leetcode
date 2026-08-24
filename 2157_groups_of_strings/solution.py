# LeetCode 2157 - Groups of Strings
# https://leetcode.com/problems/groups-of-strings/

from typing import List
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        parent = {}
        size = {}
        def find(x):
            if parent.get(x) != x:
                parent[x] = find(parent.get(x))
            return parent.get(x)

        def unite(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            if size.get(ra) < size.get(rb):
                t = ra
                ra = rb
                rb = t
            parent[rb] = ra
            size[ra] = size.get(ra) + size.get(rb)

        def maskOf(w):
            m = 0
            for i in range(len(w)):
                m |= 1 << (ord(w[i]) - 97)
            return m

        freq = {}
        for w in words:
            m = maskOf(w)
            freq[m] = (freq.get(m) or 0) + 1
        for k, v in freq.items():
            parent[k] = k
            size[k] = v
        for m in list(list(freq.keys())):
            for b in range(26):
                if (m & (1 << b)) != 0:
                    nm = m ^ (1 << b)
                    if nm in freq:
                        unite(m, nm)
                    for a in range(26):
                        if (nm & (1 << a)) == 0:
                            rm = nm | (1 << a)
                            if rm in freq:
                                unite(m, rm)
                else:
                    nm = m | (1 << b)
                    if nm in freq:
                        unite(m, nm)
        groups = 0
        maxSize = 0
        seen = set()
        for m in list(freq.keys()):
            r = find(m)
            if r not in seen:
                seen.add(r)
                groups += 1
                maxSize = max(maxSize, size.get(r))
        return [groups, maxSize]
