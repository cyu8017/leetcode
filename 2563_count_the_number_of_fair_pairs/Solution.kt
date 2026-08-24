// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution {
    fun countFairPairs(nums: IntArray, lower: Int, upper: Int): Long {
        nums.sort()
        return count(nums, upper) - count(nums, lower - 1)
    }

    private fun count(nums: IntArray, x: Int): Long {
        var ans = 0
        var l = 0
        var r = nums.size - 1
        while (l < r) {
            if (nums[l] + nums[r] <= x) {
                ans += r - l
                l = l + 1
            } else { r = r - 1 }
        }
        return ans
    }
}
