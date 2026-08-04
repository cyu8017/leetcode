// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

class Solution {
    private val memo = mutableMapOf<String, Int>()

    fun minKnightMoves(x: Int, y: Int): Int = dfs(kotlin.math.abs(x), kotlin.math.abs(y))

    private fun dfs(a: Int, b: Int): Int {
        if (a + b == 0) return 0
        if (a + b == 2) return 2
        val key = "$a,$b"
        memo[key]?.let { return it }
        val ans = minOf(dfs(kotlin.math.abs(a - 1), kotlin.math.abs(b - 2)), dfs(kotlin.math.abs(a - 2), kotlin.math.abs(b - 1))) + 1
        memo[key] = ans
        return ans
    }
}
