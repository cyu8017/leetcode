// LeetCode 3203 - Find Minimum Diameter After Merging Two Trees
// https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

class Solution {
    private var ans = 0
    private var a = 0
    private lateinit var g: Array<MutableList<Int>>

    fun minimumDiameterAfterMerge(edges1: Array<IntArray>, edges2: Array<IntArray>): Int {
        val d1 = treeDiameter(edges1)
        val d2 = treeDiameter(edges2)
        return maxOf(d1, d2, (d1 + 1) / 2 + (d2 + 1) / 2 + 1)
    }

    private fun treeDiameter(edges: Array<IntArray>): Int {
        val n = edges.size + 1
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        ans = 0
        a = 0
        dfs(0, -1, 0)
        dfs(a, -1, 0)
        return ans
    }

    private fun dfs(i: Int, fa: Int, t: Int) {
        for (j in g[i]) {
            if (j != fa) dfs(j, i, t + 1)
        }
        if (ans < t) {
            ans = t
            a = i
        }
    }
}
