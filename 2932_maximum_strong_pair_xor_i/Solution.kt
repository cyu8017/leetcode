// LeetCode 2932 - Maximum Strong Pair XOR I
// https://leetcode.com/problems/maximum-strong-pair-xor-i/


class Solution {
    fun maximumStrongPairXor(nums: IntArray): Int {
        var ans = 0
        for (i in nums.indices) {
            for (j in i until nums.size) {
                val x = nums[i]
                val y = nums[j]
                if (kotlin.math.abs(x - y) <= minOf(x, y)) {
                    val xorr = x xor y
                    if (xorr > ans) ans = xorr
                }
            }
        }
        return ans
    }
}
