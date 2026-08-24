// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution {
    private fun buildTree(n: Int, edges: Array<IntArray>): Array<ArrayList<Int>> {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        return g
    }

    private fun bipartiteCount(g: Array<ArrayList<Int>>, color: IntArray): IntArray {
        color.fill(-1)
        val q = ArrayDeque<Int>()
        q.add(0)
        color[0] = 0
        val cnt = intArrayOf(1, 0)
        while (q.isNotEmpty()) {
            val u = q.removeFirst()
            for (v in g[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] xor 1
                    cnt[color[v]]++
                    q.add(v)
                }
            }
        }
        return cnt
    }

    fun maxTargetNodes(edges1: Array<IntArray>, edges2: Array<IntArray>): IntArray {
        val n = edges1.size + 1
        val m = edges2.size + 1
        val g1 = buildTree(n, edges1)
        val g2 = buildTree(m, edges2)
        val color1 = IntArray(n)
        val color2 = IntArray(m)
        val c1 = bipartiteCount(g1, color1)
        val c2 = bipartiteCount(g2, color2)
        val best2 = maxOf(c2[0], c2[1])
        val ans = IntArray(n)
        for (i in 0 until n) ans[i] = c1[color1[i]] + best2
        return ans
    }
}
