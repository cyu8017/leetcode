// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

class Solution {
    fun findRotateSteps(ring: String, key: String): Int {
        val positions = mutableMapOf<Char, MutableList<Int>>()
        for (index in ring.indices) {
            positions.getOrPut(ring[index]) { mutableListOf() }.add(index)
        }
        val memo = mutableMapOf<Pair<Int, Int>, Int>()
        fun dp(ringIndex: Int, keyIndex: Int): Int {
            if (keyIndex == key.length) {
                return 0
            }
            val state = ringIndex to keyIndex
            memo[state]?.let { return it }
            var best = Int.MAX_VALUE
            for (pos in positions[key[keyIndex]]!!) {
                val clockwise = (pos - ringIndex + ring.length) % ring.length
                val counter = (ringIndex - pos + ring.length) % ring.length
                val steps = minOf(clockwise, counter) + 1
                best = minOf(best, steps + dp(pos, keyIndex + 1))
            }
            memo[state] = best
            return best
        }
        return dp(0, 0)
    }
}
