// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution {
    fun minLength(s: String): Int {
        val st = StringBuilder()
        for (c in s) {
            val len = st.length
            if (len > 0 && ((st[len - 1] == 'A' && c == 'B') || (st[len - 1] == 'C' && c == 'D')))
                st.setLength(len - 1)
            else st.append(c)
        }
        return st.length
    }
}
