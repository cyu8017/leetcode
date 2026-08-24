// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

class Solution {
    fun minOperations(nums: IntArray): Long {
        var ans = 0
        for (i in 1 until nums.size) {
            ans += maxOf(0L, nums[i - 1] - nums[i])
        }
        return ans
    }
}
