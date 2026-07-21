// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution {
    fun minimumXORSum(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        val dp = IntArray(1 shl n) { Int.MAX_VALUE / 2 }
        dp[0] = 0
        for (mask in 0 until (1 shl n)) {
            val i = Integer.bitCount(mask)
            if (i >= n) continue
            for (j in 0 until n) {
                if (mask and (1 shl j) != 0) continue
                val nextMask = mask or (1 shl j)
                val cost = dp[mask] + (nums1[i] xor nums2[j])
                if (cost < dp[nextMask]) dp[nextMask] = cost
            }
        }
        return dp[(1 shl n) - 1]
    }
}
