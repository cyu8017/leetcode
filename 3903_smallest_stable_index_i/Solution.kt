// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

class Solution {
    fun firstStableIndex(nums: IntArray, k: Int): Int {
        var n = nums.size
        var right = IntArray(n)
        right[n - 1] = nums[n - 1]
        run {
            var i = n - 2
            while (i >= 0) {
                right[i] = minOf(right[i + 1], nums[i])
                i--
            }
        }
        var left = 0
        for (i in 0 until n) {
            left = maxOf(left, nums[i])
            if (left - right[i] <= k) return i
        }
        return -1
    }
}
