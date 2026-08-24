// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

class Solution {
    fun superEggDrop(k: Int, n: Int): Int {
        var dp = IntArray(k + 1)
        var moves = 0
        while (dp[k] < n) {
            moves++
            for (eggs in k downTo 1) {
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
            }
        }
        return moves
    }
}
