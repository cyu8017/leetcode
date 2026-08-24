// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution {
    fun minDifference(nums: IntArray): Int {
        if (nums.size <= 4) return 0
        nums.sort()
        var ans = Int.MAX_VALUE
        for (i in 0 until 4) {
            ans = minOf(ans, nums[nums.size - 4 + i] - nums[i])
        }
        return ans
    }
}
