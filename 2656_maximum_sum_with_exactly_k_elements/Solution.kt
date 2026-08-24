// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
    fun maximizeSum(nums: IntArray, k: Int): Int {
        var mx = nums[0]
        for (x in nums) if (x > mx) mx = x
        return k * mx + k * (k - 1) / 2
    }
}
