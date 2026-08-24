// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

import java.util.ArrayDeque

class Solution {
    fun reachableNodes(n: Int, edges: Array<IntArray>, restricted: IntArray): Int {
        val ban = restricted.toHashSet()
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        var ans = 0
        val vis = BooleanArray(n)
        val q = ArrayDeque<Int>()
        q.offer(0)
        vis[0] = true
        while (q.isNotEmpty()) {
            val u = q.poll()
            ans++
            for (v in g[u]) {
                if (!vis[v] && v !in ban) {
                    vis[v] = true
                    q.offer(v)
                }
            }
        }
        return ans
    }
}
