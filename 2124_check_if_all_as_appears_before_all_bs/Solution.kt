// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution {
    fun checkString(s: String): Boolean {
        var seenB: Boolean = false
        for (i in 0 until s.length) {
            var c: Char = s[i]
            if (c == 'b') seenB = true
            else if (seenB) return false
        }
        return true
    }
}
