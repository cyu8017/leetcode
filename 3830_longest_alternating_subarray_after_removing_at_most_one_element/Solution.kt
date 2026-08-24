// LeetCode 3830 - Longest Alternating Subarray After Removing At Most One Element
// https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

class Solution {
    fun longestAlternating(nums: IntArray): Int {
        var n = nums.size
        var l1 = IntArray(n)
        var l2 = IntArray(n)
        var r1 = IntArray(n)
        var r2 = IntArray(n)
        l1.fill(1); l2.fill(1); r1.fill(1); r2.fill(1)
        var ans = 0
        for (i in 1 until n) {
            if (nums[i - 1] < nums[i]) l1[i] = l2[i - 1] + 1
            else if (nums[i - 1] > nums[i]) l2[i] = l1[i - 1] + 1
            ans = maxOf(ans, maxOf(l1[i], l2[i]))
        }
        for (i in n - 2 downTo 0) {
            if (nums[i + 1] > nums[i]) r1[i] = r2[i + 1] + 1
            else if (nums[i + 1] < nums[i]) r2[i] = r1[i + 1] + 1
        }
        for (i in 1 until n - 1) {
            if (nums[i - 1] < nums[i + 1]) ans = maxOf(ans, l2[i - 1] + r2[i + 1])
            else if (nums[i - 1] > nums[i + 1]) ans = maxOf(ans, l1[i - 1] + r1[i + 1])
        }
        return ans
    }
}
