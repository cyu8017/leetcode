# LeetCode 0839 - Similar String Groups
# https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n = len(strs)
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def similar(a: str, b: str) -> bool:
            diff = [i for i in range(len(a)) if a[i] != b[i]]
            return len(diff) == 0 or (
                len(diff) == 2 and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]]
            )

        groups = n
        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    pi, pj = find(i), find(j)
                    if pi != pj:
                        parent[pi] = pj
                        groups -= 1
        return groups
