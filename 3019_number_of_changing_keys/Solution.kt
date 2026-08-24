// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

class Solution {
    fun countKeyChanges(s0: String): Int {
        val s = s0.lowercase()
        var ans = 0
        for (i in 1 until s.length) {
            if (s[i] != s[i - 1]) ans++
        }
        return ans
    }
}
