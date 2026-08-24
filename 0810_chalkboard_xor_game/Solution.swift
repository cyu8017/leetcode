// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

class Solution {
    func xorGame(_ nums: [Int]) -> Bool {
        var x = 0
        for num in nums { x ^= num }
        return x == 0 || nums.count % 2 == 0
    }
}
