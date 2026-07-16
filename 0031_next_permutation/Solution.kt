// LeetCode 0031 - Next Permutation
// https://leetcode.com/problems/next-permutation/

class Solution {
    fun nextPermutation(nums: IntArray) {
        var i = nums.size - 2
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--
        }

        if (i >= 0) {
            var j = nums.size - 1
            while (nums[j] <= nums[i]) {
                j--
            }
            val tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        }

        var left = i + 1
        var right = nums.size - 1
        while (left < right) {
            val tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left++
            right--
        }
    }
}
