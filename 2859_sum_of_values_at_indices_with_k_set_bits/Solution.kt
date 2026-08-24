// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution {
    fun sumIndicesWithKSetBits(nums: MutableList<Int>, k: Int): Int {
        var ans = 0
        for (i in 0 until nums.size) {
            if (Integer.bitCount(i) == k) ans += nums[i]
        }
        return ans
    }
}
