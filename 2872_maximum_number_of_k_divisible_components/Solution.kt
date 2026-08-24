// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/


class Solution {
    private lateinit var g: Array<MutableList<Int>>
    private lateinit var values: IntArray
    private var k = 0
    private var ans = 0

    fun maxKDivisibleComponents(n: Int, edges: Array<IntArray>, values: IntArray, k: Int): Int {
        this.values = values
        this.k = k
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        ans = 0
        dfs(0, -1)
        return ans
    }

    private fun dfs(u: Int, p: Int): Int {
        var sum = values[u] % k
        for (v in g[u]) {
            if (v == p) continue
            sum = (sum + dfs(v, u)) % k
        }
        if (sum == 0) ans++
        return sum
    }
}
