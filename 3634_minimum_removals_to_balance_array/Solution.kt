// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution {
    fun minRemoval(nums: IntArray, k: Int): Int {
        nums.sort()
        var n = nums.size
        var cnt = 0
        for (i in 0 until n) {
            var j = n
            if (1L * nums[i] * k <= nums[n - 1]) {
                var target = 1L * nums[i] * k + 1
                j = lowerBound(nums, target)
            }
            cnt = maxOf(cnt, j - i)
        }
        return n - cnt
    }

    private fun lowerBound(a: IntArray, target: Long): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (a[mid] < target) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
