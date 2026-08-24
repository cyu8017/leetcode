// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

class Solution {
    fun residuePrefixes(s: String): Int {
        val st = HashSet<Char>()
        var ans = 0
        for (i in s.indices) {
            st.add(s[i])
            if (st.size == (i + 1) % 3) ans++
        }
        return ans
    }
}
