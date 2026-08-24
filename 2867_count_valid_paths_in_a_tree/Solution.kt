// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/


class Solution {
    private lateinit var isPrime: BooleanArray
    private lateinit var g: Array<MutableList<Int>>

    fun countPaths(n: Int, edges: Array<IntArray>): Long {
        isPrime = BooleanArray(n + 1) { true }
        isPrime[0] = false
        isPrime[1] = false
        var i = 2
        while (i * i <= n) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= n) {
                    isPrime[j] = false
                    j += i
                }
            }
            i++
        }
        g = Array(n + 1) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        var ans = 0L
        for (u in 1..n) {
            if (!isPrime[u]) continue
            var total = 0L
            for (v in g[u]) {
                val c = dfs(v, u).toLong()
                ans += c
                ans += total * c
                total += c
            }
        }
        return ans
    }

    private fun dfs(u: Int, p: Int): Int {
        if (isPrime[u]) return 0
        var sz = 1
        for (v in g[u]) if (v != p) sz += dfs(v, u)
        return sz
    }
}
