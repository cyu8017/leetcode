// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution {
    fun minimumJumps(forbidden: IntArray, a: Int, b: Int, x: Int): Int {
        val bad = forbidden.toHashSet()
        val limit = maxOf(x, forbidden.maxOrNull() ?: 0) + a + b
        val q = ArrayDeque<IntArray>()
        q.add(intArrayOf(0, 0, 0))
        val seen = HashSet<Long>()
        seen.add(0L)
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            val p = cur[0]
            val d = cur[1]
            val back = cur[2] == 1
            if (p == x) return d
            val candidates = listOf(p + a to false, p - b to true)
            for ((np, nb) in candidates) {
                if (np < 0 || np > limit || np in bad) continue
                if (back && nb) continue
                val key = (np.toLong() shl 1) or (if (nb) 1L else 0L)
                if (key in seen) continue
                seen.add(key)
                q.add(intArrayOf(np, d + 1, if (nb) 1 else 0))
            }
        }
        return -1
    }
}
