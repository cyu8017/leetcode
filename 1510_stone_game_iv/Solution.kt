// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

class Solution {
    fun winnerSquareGame(n: Int): Boolean {
        val win = BooleanArray(n + 1)
        for (value in 1..n) {
            var root = 1
            while (root * root <= value) {
                if (!win[value - root * root]) {
                    win[value] = true
                    break
                }
                root++
            }
        }
        return win[n]
    }
}
