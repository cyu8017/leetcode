// LeetCode 1908 - Game Of Nim
// https://leetcode.com/problems/game-of-nim/

class Solution {
    fun nimGame(piles: IntArray): Boolean {
        var x = 0
        for (p in piles) x = x xor p
        return x != 0
    }
}
