// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

class Solution {
    fun xorGame(nums: IntArray): Boolean {
        var x = 0
        for (num in nums) { x ^= num }
        return x == 0 || nums.size % 2 == 0
    }
}
