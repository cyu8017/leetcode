// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

class Solution {
    private val memo = mutableMapOf<String, Int>()

    fun findMinStep(board: String, hand: String): Int {
        val result = dfs(board, hand)
        return if (result == Int.MAX_VALUE) -1 else result
    }

    private fun dfs(board: String, hand: String): Int {
        val key = "$board|$hand"
        memo[key]?.let { return it }
        val shrunk = shrink(board)
        if (shrunk.isEmpty()) {
            memo[key] = 0
            return 0
        }
        var best = Int.MAX_VALUE
        for (i in 0..shrunk.length) {
            for (j in hand.indices) {
                val color = hand[j]
                val valid = (i < shrunk.length && shrunk[i] == color)
                    || (i > 0 && shrunk[i - 1] == color)
                if (!valid) {
                    continue
                }
                val newBoard = shrink(shrunk.substring(0, i) + color + shrunk.substring(i))
                if (newBoard == shrunk) {
                    continue
                }
                val newHand = hand.removeRange(j, j + 1)
                val steps = dfs(newBoard, newHand)
                if (steps != Int.MAX_VALUE) {
                    best = minOf(best, steps + 1)
                }
            }
        }
        memo[key] = best
        return best
    }

    private fun shrink(s: String): String {
        var i = 0
        while (i < s.length) {
            var j = i
            while (j < s.length && s[j] == s[i]) {
                j += 1
            }
            if (j - i >= 3) {
                return shrink(s.substring(0, i) + s.substring(j))
            }
            i = j
        }
        return s
    }
}
