// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

class Solution {
    fun longestSubarray(nums: IntArray): Int {
        var n = nums.size
        var left = IntArray(n)
        var right = IntArray(n)
        var i: Int = 0
while (i < n) {
 left[i] = 1; right[i] = 1
i = i + 1
}
        for (i in 1 until n) {
            if (nums[i] >= nums[i - 1]) left[i] = left[i - 1] + 1
        }
        for (i in n - 2 downTo 0) {
            if (nums[i] <= nums[i + 1]) right[i] = right[i + 1] + 1
        }
        var ans = 0
        for (v in left) { ans = maxOf(ans, v) }
        for (i in 0 until n) {
            var a = if (i > 0) left[i - 1] else 0
            var b = if (i + 1 < n) right[i + 1] else 0
            if (i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1]) {
                ans = maxOf(ans, maxOf(a + 1, b + 1))
            } else {
                ans = maxOf(ans, a + b + 1)
            }
        }
        return ans
    }
}
