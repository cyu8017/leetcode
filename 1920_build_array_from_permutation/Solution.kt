// LeetCode 1920 - Build Array From Permutation
// https://leetcode.com/problems/build-array-from-permutation/

class Solution {
    fun buildArray(nums: IntArray): IntArray = IntArray(nums.size) { nums[nums[it]] }
}
