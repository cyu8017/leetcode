// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution {
    fun minFlipsMonoIncr(s: String): Int {
        var ones = 0
        var ans = 0
        for (ch in s) {
            if (ch == '1') ones++
            else ans = minOf(ans + 1, ones)
        }
        return ans
    }
}
