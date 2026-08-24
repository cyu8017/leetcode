// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

class Solution {
    fun countValidPrefixes(s: String): Int {
        var ans = 0
        var t = 0
        for (i in 0 until s.length) {
            if (s[i] == '1') t++
            else t--
            if (t >= -1 && t <= 1) ans++
        }
        return ans
    }
}
