// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

class Solution {
    fun threeSumSmaller(nums: IntArray, target: Int): Int {
        nums.sort()
        var count = 0
        for (index in 0 until nums.size - 2) {
            var left = index + 1
            var right = nums.size - 1
            while (left < right) {
                val total = nums[index] + nums[left] + nums[right]
                if (total < target) {
                    count += right - left
                    left++
                } else {
                    right--
                }
            }
        }
        return count
    }
}
