// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

class Solution {
    fun minimumOperationsToMakeEqual(x: Int, y: Int): Int {
        if (x <= y) return y - x
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(x, 0))
        val seen = HashSet<Int>()
        seen.add(x)
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val v = cur[0]
            val d = cur[1]
            if (v == y) return d
            val cands = intArrayOf(
                v + 1,
                v - 1,
                if (v % 11 == 0) v / 11 else -1,
                if (v % 5 == 0) v / 5 else -1
            )
            for (nxt in cands) {
                if (nxt > 0 && nxt < 2 * x + 20 && seen.add(nxt)) {
                    q.add(intArrayOf(nxt, d + 1))
                }
            }
        }
        return -1
    }
}
