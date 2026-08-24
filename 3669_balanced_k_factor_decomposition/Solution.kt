// LeetCode 3669 - Balanced K-Factor Decomposition
// https://leetcode.com/problems/balanced-k-factor-decomposition/

class Solution {
    companion object {
        private const val MX = 100001
        private var g: Array<ArrayList<Int>>? = null
        private var inited = false

        private fun ensureInit() {
            if (inited) return
            val gg = Array(MX) { ArrayList<Int>() }
            for (i in 1 until MX) {
                var j = i
                while (j < MX) {
                    gg[j].add(i)
                    j += i
                }
            }
            g = gg
            inited = true
        }
    }

    private var cur = 0
    private lateinit var ans: IntArray
    private lateinit var path: IntArray

    private fun dfs(i: Int, x: Int, mi: Int, mx: Int) {
        if (i == 0) {
            val d = maxOf(mx, x) - minOf(mi, x)
            if (d < cur) {
                cur = d
                path[i] = x
                ans = path.clone()
            }
            return
        }
        for (y in g!![x]) {
            path[i] = y
            dfs(i - 1, x / y, minOf(mi, y), maxOf(mx, y))
        }
    }

    fun minDifference(n: Int, k: Int): IntArray {
        ensureInit()
        cur = Int.MAX_VALUE
        ans = IntArray(0)
        path = IntArray(k)
        dfs(k - 1, n, Int.MAX_VALUE, 0)
        return ans
    }
}
