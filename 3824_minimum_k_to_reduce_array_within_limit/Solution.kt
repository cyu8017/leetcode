// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

class Solution {
    fun minimumK(nums: IntArray): Int {
        var lo = 1
        var hi = 100000
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (check(nums, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun check(nums: IntArray, k: Int): Boolean {
        var t = 0
        for (x in nums) { t += (x + k - 1) / k }
        return t <= 1L * k * k
    }
}
