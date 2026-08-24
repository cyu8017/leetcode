// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var colors: IntArray
    private lateinit var size: IntArray
    private var ans = 0

    private fun dfs(a: Int, fa: Int): Boolean {
        size[a] = 1
        var ok = true
        for (b in g[a]) if (b != fa) {
            val t = dfs(b, a)
            ok = ok && t && colors[a] == colors[b]
            size[a] += size[b]
        }
        if (ok) ans = maxOf(ans, size[a])
        return ok
    }

    fun maximumSubtreeSize(edges: Array<IntArray>, colors: IntArray): Int {
        val n = edges.size + 1
        g = Array(n) { ArrayList() }
        for (e in edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]) }
        this.colors = colors
        size = IntArray(n)
        ans = 0
        dfs(0, -1)
        return ans
    }
}
