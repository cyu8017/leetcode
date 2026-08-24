// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

class Solution {
    fun minDifference(nums: IntArray): Int {
        var n = nums.size
        var lo = 0
        var hi = 1_000_000_000
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (ok(mid, nums, n)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun ok(d: Int, nums: IntArray, n: Int): Boolean {
        var prev = -1
        for (i in 0 until n) {
            if (nums[i] != -1) {
                if (prev != -1 && kotlin.math.abs(nums[i] - prev) > d) return false
                prev = nums[i]
                continue
            }
            var j = i
            while (j < n && nums[j] == -1) j++
            var left = prev
            var right = if ((j < n)) nums[j] else -1
            var gap = j - i
            if (left == -1 && right == -1) return true
            if (left == -1 || right == -1) {
                prev = -1
                i = j - 1
                continue
            }
            if (kotlin.math.abs(left - right) > d * (gap + 1L)) return false
            prev = -1
            i = j - 1
        }
        return true
    }
}
