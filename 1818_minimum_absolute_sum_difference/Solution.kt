// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

class Solution {
    fun minAbsoluteSumDiff(nums1: IntArray, nums2: IntArray): Int {
        val mod = 1_000_000_007
        val sorted = nums1.sorted()
        var total = 0L
        var bestGain = 0
        for (i in nums1.indices) {
            val current = kotlin.math.abs(nums1[i] - nums2[i])
            total += current
            val target = nums2[i]
            var lo = 0
            var hi = sorted.size
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (sorted[mid] < target) lo = mid + 1 else hi = mid
            }
            for (j in listOf(lo - 1, lo)) {
                if (j in sorted.indices) {
                    bestGain = maxOf(bestGain, current - kotlin.math.abs(sorted[j] - target))
                }
            }
        }
        return ((total - bestGain) % mod).toInt()
    }
}
