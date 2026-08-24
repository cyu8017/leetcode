// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution {
    fun isWinner(player1: IntArray, player2: IntArray): Int {
        val a = score(player1)
        val b = score(player2)
        if (a > b) return 1
        if (b > a) return 2
        return 0
    }

    private fun score(p: IntArray): Int {
        var s = 0
        for (i in p.indices) {
            var mul = 1
            if ((i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10)) mul = 2
            s += mul * p[i]
        }
        return s
    }
}
