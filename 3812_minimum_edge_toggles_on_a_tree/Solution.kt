// LeetCode 3812 - Minimum Edge Toggles On A Tree
// https://leetcode.com/problems/minimum_edge_toggles_on_a_tree/

class Solution {
    private lateinit var g: Array<ArrayList<IntArray>>
    private lateinit var start: String
    private lateinit var target: String
    private lateinit var ans: ArrayList<Int>

    fun minimumFlips(n: Int, edges: Array<IntArray>, start: String, target: String): IntArray {
        this.start = start
        this.target = target
        g = Array(n) { ArrayList() }
        for (i in 0 until n - 1) {
            val a = edges[i][0]
            val b = edges[i][1]
            g[a].add(intArrayOf(b, i))
            g[b].add(intArrayOf(a, i))
        }
        ans = ArrayList()
        if (dfs(0, -1)) return intArrayOf(-1)
        ans.sort()
        return ans.toIntArray()
    }

    private fun dfs(a: Int, fa: Int): Boolean {
        var rev = start[a] != target[a]
        for (e in g[a]) {
            val b = e[0]
            val i = e[1]
            if (b != fa && dfs(b, a)) {
                ans.add(i)
                rev = !rev
            }
        }
        return rev
    }
}
