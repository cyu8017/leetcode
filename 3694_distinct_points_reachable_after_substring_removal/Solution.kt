// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

class Solution {
    fun distinctPoints(s: String, k: Int): Int {
        val n = s.length
        val f = IntArray(n + 1)
        val g = IntArray(n + 1)
        var x = 0
        var y = 0
        for (i in 1..n) {
            when (s[i - 1]) {
                'U' -> y++
                'D' -> y--
                'L' -> x--
                else -> x++
            }
            f[i] = x
            g[i] = y
        }
        val st = HashSet<Long>()
        for (i in k..n) {
            val a = f[n] - (f[i] - f[i - k])
            val b = g[n] - (g[i] - g[i - k])
            val key = a.toLong() * n + b
            st.add(key)
        }
        return st.size
    }
}
