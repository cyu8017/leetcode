// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

class Solution {

    fun distanceToCycle(n: Int, edges: Array<IntArray>): IntArray {

            @SuppressWarnings("unchecked")
            var g = arrayOfNulls<ArrayList>(n)
            for (i in 0 until n) { g[i] = ArrayList<Int>() }
            var deg = IntArray(n)
            for (e in edges) {
                g[e[0]].add(e[1])
                g[e[1]].add(e[0])
                deg[e[0]]++
                deg[e[1]]++
            }
            var q = ArrayDeque<Int>()
            for (i in 0 until n) { if (deg[i] == 1) q.offer(i) }
            var onCycle = BooleanArray(n)
            for (i in 0 until n) { onCycle[i] = true }
            while (!q.isEmpty()) {
                var u = q.poll()
                onCycle[u] = false
                for (v in g[u]) {
                    if (--deg[v] == 1) q.offer(v)
                }
            }
            var ans = IntArray(n)
            for (i in 0 until n) { ans[i] = -1 }
            var qq = ArrayDeque<Int>()
            for (i in 0 until n) { if (onCycle[i]) {
                ans[i] = 0 }
                qq.offer(i)
            }
            while (!qq.isEmpty()) {
                var u = qq.poll()
                for (v in g[u]) if (ans[v] == -1) {
                    ans[v] = ans[u] + 1
                    qq.offer(v)
                }
            }
            return ans

    }

}
