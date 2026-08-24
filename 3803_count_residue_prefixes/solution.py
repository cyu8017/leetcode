# LeetCode 3803 - Count Residue Prefixes
# https://leetcode.com/problems/count-residue-prefixes/

class Solution:
    def residuePrefixes(self, s: str) -> int:
        st = set()
        ans = 0
        for i, ch in enumerate(s):
            st.add(ch)
            if len(st) == (i + 1) % 3:
                ans += 1
        return ans
