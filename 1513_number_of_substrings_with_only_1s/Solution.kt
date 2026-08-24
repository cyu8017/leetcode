// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution {
    fun numSub(s: String): Int {
        val mod = 1_000_000_007
        var ans = 0L
        var run = 0
        for (ch in s) {
            if (ch == '1') {
                run++
                ans += run
            } else {
                run = 0
            }
        }
        return (ans % mod).toInt()
    }
}
