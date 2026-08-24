# LeetCode 2696 - Minimum String Length After Removing Substrings
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for c in s:
            last = st[-1] if st else None
            if st and ((last == "A" and c == "B") or (last == "C" and c == "D")):
                st.pop()
            else:
                st.append(c)
        return len(st)
