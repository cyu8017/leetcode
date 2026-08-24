// LeetCode 3350 - Adjacent Increasing Subarrays Detection II
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution {
    fun maxIncreasingSubarrays(nums: MutableList<Int>): Int {
        var n = nums.size
        var up = IntArray(n)
        up[n - 1] = 1
        for (i in n - 2 downTo 0) {
            up[i] =if ((nums[i] < nums[i + 1])) up[i + 1] + 1 else 1
        }
        var lo = 1
        var hi = n / 2
        while (lo < hi) {
            var mid = (lo + hi + 1) / 2
            if (ok(up, n, mid)) lo = mid
            else hi = mid - 1
        }
        return lo
    }

    private fun ok(up: IntArray, n: Int, k: Int): Boolean {
        var i = 0
        while (i + 2 * k <= n) {
            if (up[i] >= k && up[i + k] >= k) return true
            i++
        }
        return false
    }
}
