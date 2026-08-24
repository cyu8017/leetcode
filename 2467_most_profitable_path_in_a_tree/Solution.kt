// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var amount: IntArray
    private lateinit var bobTime: IntArray
    private var ans = 0

    private fun findBob(u: Int, p: Int, t: Int): Boolean {
        if (u == 0) {
            bobTime[u] = t
            return true
        }
        for (v in g[u]) {
            if (v == p) continue
            if (findBob(v, u, t + 1)) {
                bobTime[u] = t
                return true
            }
        }
        return false
    }

    private fun dfs(u: Int, p: Int, t: Int, incomeIn: Int) {
        var cur = amount[u]
        if (t > bobTime[u]) cur = 0
        else if (t == bobTime[u]) cur /= 2
        val income = incomeIn + cur
        var isLeaf = true
        for (v in g[u]) {
            if (v != p) {
                isLeaf = false
                dfs(v, u, t + 1, income)
            }
        }
        if (isLeaf && income > ans) ans = income
    }

    fun mostProfitablePath(edges: Array<IntArray>, bob: Int, amount: IntArray): Int {
        this.amount = amount
        val n = amount.size
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        bobTime = IntArray(n) { n }
        findBob(bob, -1, 0)
        ans = Int.MIN_VALUE
        dfs(0, -1, 0, 0)
        return ans
    }
}
