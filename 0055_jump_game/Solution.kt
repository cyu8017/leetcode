// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

class Solution {
    fun canJump(nums: IntArray): Boolean {
        var farthest = 0

        for (i in nums.indices) {
            if (i > farthest) {
                return false
            }
            farthest = maxOf(farthest, i + nums[i])
        }

        return true
    }
}
