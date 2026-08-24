// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

class Solution {
    fun finalElement(nums: IntArray): Int {
        return maxOf(nums[0], nums[nums.size - 1])
    }
}
