// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

class Solution {
    private class MarkNode(var node: Int = 0, var time: Int = 0)

    private class Top2 {
        var top1 = MarkNode()
        var top2 = MarkNode()
    }

    private lateinit var tree: Array<MutableList<Int>>
    private lateinit var dp: Array<Top2>
    private lateinit var ans: IntArray

    fun timeTaken(edges: Array<IntArray>): IntArray {
        val n = edges.size + 1
        ans = IntArray(n)
        tree = Array(n) { ArrayList() }
        dp = Array(n) { Top2() }
        for (e in edges) {
            tree[e[0]].add(e[1])
            tree[e[1]].add(e[0])
        }
        dfs(0, -1)
        reroot(0, -1, 0)
        return ans
    }

    private fun getTime(u: Int): Int = if (u % 2 == 0) 2 else 1

    private fun dfs(u: Int, prev: Int): Int {
        var t1 = MarkNode()
        var t2 = MarkNode()
        for (v in tree[u]) {
            if (v == prev) continue
            val t = dfs(v, u) + getTime(v)
            if (t >= t1.time) {
                t2 = t1
                t1 = MarkNode(v, t)
            } else if (t > t2.time) {
                t2 = MarkNode(v, t)
            }
        }
        dp[u].top1 = t1
        dp[u].top2 = t2
        return t1.time
    }

    private fun reroot(u: Int, prev: Int, maxTime: Int) {
        ans[u] = maxTime
        if (dp[u].top1.time > ans[u]) ans[u] = dp[u].top1.time
        for (v in tree[u]) {
            if (v == prev) continue
            var side = dp[u].top1.time
            if (dp[u].top1.node == v) side = dp[u].top2.time
            val newMax = maxOf(maxTime, side)
            reroot(v, u, getTime(u) + newMax)
        }
    }
}
