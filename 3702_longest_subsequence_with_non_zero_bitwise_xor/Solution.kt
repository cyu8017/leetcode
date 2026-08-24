// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

class Solution {
    fun longestSubsequence(nums: IntArray): Int {
        var xorv = 0
        var cnt0 = 0
        for (x in nums) {
            xorv ^= x
            if (x == 0) cnt0++
        }
        var n = nums.size
        if (xorv != 0) return n
        if (cnt0 == n) return 0
        return n - 1
    }
}
