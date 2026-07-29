// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution {
    fun missingElement(nums: IntArray, k: Int): Int {
        val n = nums.size
        if (k > missing(nums, n - 1)) {
            return nums[n - 1] + k - missing(nums, n - 1)
        }
        var lo = 0
        var hi = n - 1
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (missing(nums, mid) < k) lo = mid + 1 else hi = mid
        }
        return nums[lo - 1] + k - missing(nums, lo - 1)
    }

    private fun missing(nums: IntArray, i: Int): Int = nums[i] - nums[0] - i
}
