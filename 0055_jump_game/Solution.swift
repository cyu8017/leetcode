// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        var farthest = 0

        for (i, jump) in nums.enumerated() {
            if i > farthest {
                return false
            }
            farthest = max(farthest, i + jump)
        }

        return true
    }
}
