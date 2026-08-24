// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

class Solution {
    private lateinit var graph: Array<ArrayList<Int>>
    private lateinit var ks: IntArray
    private lateinit var freq: HashMap<Int, Int>
    private var ans = 0L

    private fun kernel(x0: Int): Int {
        var x = x0
        var res = 1
        var p = 2
        while (p * p <= x) {
            var cnt = 0
            while (x % p == 0) {
                x /= p
                cnt++
            }
            if (cnt % 2 == 1) res *= p
            p++
        }
        if (x > 1) res *= x
        return res
    }

    private fun dfs(u: Int, p: Int) {
        ans += freq.getOrDefault(ks[u], 0)
        freq.merge(ks[u], 1) { a, b -> a + b }
        for (v in graph[u]) if (v != p) dfs(v, u)
        freq.merge(ks[u], -1) { a, b -> a + b }
    }

    fun sumOfAncestors(n: Int, edges: Array<IntArray>, nums: IntArray): Long {
        graph = Array(n) { ArrayList() }
        for (e in edges) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        ks = IntArray(n)
        for (i in 0 until n) ks[i] = kernel(nums[i])
        freq = HashMap()
        ans = 0
        dfs(0, -1)
        return ans
    }
}
