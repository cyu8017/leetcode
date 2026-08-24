// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

class Solution {
    fun firstMissingPositive(nums: IntArray): Int {
        val n = nums.size
        var i = 0

        while (i < n) {
            val value = nums[i]
            val target = value - 1
            if (value in 1..n && nums[target] != value) {
                val temp = nums[i]
                nums[i] = nums[target]
                nums[target] = temp
            } else {
                i++
            }
        }

        for (index in 0 until n) {
            if (nums[index] != index + 1) {
                return index + 1
            }
        }

        return n + 1
    }
}
