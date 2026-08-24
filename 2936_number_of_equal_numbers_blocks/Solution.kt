// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/


class Solution {
    fun blockCount(nums: List<Int>): Int {
        if (nums.isEmpty()) return 0
        var ans = 1
        for (i in 1 until nums.size) if (nums[i] != nums[i - 1]) ans++
        return ans
    }
}
