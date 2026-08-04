// LeetCode 1955
// https://leetcode.com/problems/count-number-of-special-subsequences/

class Solution {
    fun countSpecialSubsequences(nums: IntArray): Int {
        val mod = 1_000_000_007
        var a = 0
        var b = 0
        var c = 0
        for (x in nums) {
            when (x) {
                0 -> a = (a * 2 + 1) % mod
                1 -> b = (b * 2 + a) % mod
                else -> c = (c * 2 + b) % mod
            }
        }
        return c
    }
}
