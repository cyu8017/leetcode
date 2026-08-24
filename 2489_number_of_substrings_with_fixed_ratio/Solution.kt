// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

class Solution {
    fun fixedRatio(s: String, num1: Int, num2: Int): Long {
        val pref = HashMap<Long, Int>()
        pref[0L] = 1
        var zeros = 0
        var ones = 0
        var ans = 0L
        for (c in s) {
            if (c == '0') zeros++ else ones++
            val key = 1L * zeros * num2 - 1L * ones * num1
            ans += pref.getOrDefault(key, 0)
            pref[key] = pref.getOrDefault(key, 0) + 1
        }
        return ans
    }
}
