// LeetCode 1320 - Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

class Solution {
    fun minimumDistance(word: String): Int {
        fun distance(a: Int, b: Int): Int {
            if (a == 26) return 0
            return kotlin.math.abs(a / 6 - b / 6) + kotlin.math.abs(a % 6 - b % 6)
        }
        val letters = word.map { it - 'A' }
        var dp = mutableMapOf(26 to 0)
        var previous = letters[0]
        for (current in letters.drop(1)) {
            val nxt = mutableMapOf<Int, Int>()
            for ((free, cost) in dp) {
                nxt[free] = minOf(nxt.getOrDefault(free, Int.MAX_VALUE / 2), cost + distance(previous, current))
                nxt[previous] = minOf(nxt.getOrDefault(previous, Int.MAX_VALUE / 2), cost + distance(free, current))
            }
            dp = nxt
            previous = current
        }
        return dp.values.minOrNull() ?: 0
    }
}
