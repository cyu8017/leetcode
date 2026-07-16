// LeetCode 0045 - Jump Game II
// https://leetcode.com/problems/jump-game-ii/

class Solution {
    fun jump(nums: IntArray): Int {
        var jumps = 0
        var currentEnd = 0
        var farthest = 0

        for (i in 0 until nums.size - 1) {
            farthest = maxOf(farthest, i + nums[i])
            if (i == currentEnd) {
                jumps++
                currentEnd = farthest
            }
        }

        return jumps
    }
}
