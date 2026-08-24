// LeetCode 3249 - Count the Number of Good Nodes
// https://leetcode.com/problems/count-the-number-of-good-nodes/

class Solution {
    private lateinit var g: Array<MutableList<Int>>
    private var ans = 0

    fun countGoodNodes(edges: Array<IntArray>): Int {
        val n = edges.size + 1
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        ans = 0
        dfs(0, -1)
        return ans
    }

    private fun dfs(a: Int, fa: Int): Int {
        var pre = -1
        var cnt = 1
        var ok = 1
        for (b in g[a]) {
            if (b != fa) {
                val cur = dfs(b, a)
                cnt += cur
                if (pre < 0) pre = cur
                else if (pre != cur) ok = 0
            }
        }
        ans += ok
        return cnt
    }
}
