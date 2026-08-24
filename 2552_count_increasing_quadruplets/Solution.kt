// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

class Solution {
    fun countQuadruplets(nums: IntArray): Long {
        val n = nums.size
        var ans = 0L
        val great = IntArray(n)
        for (j in 0 until n) {
            for (i in 0 until j) {
                if (nums[i] < nums[j]) ans += great[i]
                else if (nums[i] > nums[j]) great[i] += 1
            }
        }
        return ans
    }
}
