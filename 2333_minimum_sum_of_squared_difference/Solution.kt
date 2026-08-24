// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

import kotlin.math.abs

class Solution {
    fun minSumSquareDiff(nums1: IntArray, nums2: IntArray, k1: Int, k2: Int): Long {
        val n = nums1.size
        val diff = IntArray(n)
        var maxD = 0
        for (i in 0 until n) {
            val d = abs(nums1[i] - nums2[i])
            diff[i] = d
            if (d > maxD) maxD = d
        }
        var k = k1 + k2
        val freq = IntArray(maxD + 1)
        for (d in diff) freq[d]++
        var d = maxD
        while (d > 0 && k > 0) {
            if (freq[d] != 0) {
                var take = freq[d]
                if (take > k) take = k
                freq[d] -= take
                freq[d - 1] += take
                k -= take
            }
            d--
        }
        var ans = 0L
        for (x in 0..maxD) ans += x.toLong() * x * freq[x]
        return ans
    }
}
