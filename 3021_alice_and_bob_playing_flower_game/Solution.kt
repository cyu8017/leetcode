// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

class Solution {
    fun flowerGame(n: Int, m: Int): Long {
        var a1 = (n + 1) / 2
        var b1 = (m + 1) / 2
        var a2 = n / 2
        var b2 = m / 2
        return a1 * b2 + a2 * b1
    }
}
