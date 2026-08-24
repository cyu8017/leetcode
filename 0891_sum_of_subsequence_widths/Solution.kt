// LeetCode 0891 - Sum of Subsequence Widths
// https://leetcode.com/problems/sum-of-subsequence-widths/

class Solution {
    fun sumSubseqWidths(nums: IntArray): Int {
        val MOD = 1_000_000_007
        nums.sort()
        val n = nums.size
        val pow2 = LongArray(n)
        pow2[0] = 1
        for (i in 1 until n) pow2[i] = (pow2[i - 1] * 2) % MOD
        var ans = 0L
        for (i in 0 until n) {
            ans = (ans + nums[i] * (pow2[i] - pow2[n - 1 - i])) % MOD
        }
        return ((ans + MOD) % MOD).toInt()
    }
}
