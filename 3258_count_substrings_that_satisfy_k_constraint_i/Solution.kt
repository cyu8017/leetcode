// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution {
    fun countKConstraintSubstrings(s: String, k: Int): Int {
        var ans = 0
        val n = s.length
        for (i in 0 until n) {
            var z = 0
            var o = 0
            for (j in i until n) {
                if (s[j] == '0') z++ else o++
                if (z <= k || o <= k) ans++
                else break
            }
        }
        return ans
    }
}
