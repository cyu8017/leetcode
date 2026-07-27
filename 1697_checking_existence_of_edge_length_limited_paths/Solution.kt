// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution {
    fun distanceLimitedPathsExist(n: Int, edgeList: Array<IntArray>, queries: Array<IntArray>): BooleanArray {
        val parent = IntArray(n) { it }
        fun find(x: Int): Int {
            var cur = x
            while (cur != parent[cur]) {
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            }
            return cur
        }
        val ans = BooleanArray(queries.size)
        val edges = edgeList.sortedBy { it[2] }
        val ordered = queries.mapIndexed { j, q -> intArrayOf(q[2], q[0], q[1], j) }
            .sortedBy { it[0] }
        var i = 0
        for (item in ordered) {
            val limit = item[0]
            val p = item[1]
            val q = item[2]
            val idx = item[3]
            while (i < edges.size && edges[i][2] < limit) {
                val a = find(edges[i][0])
                val b = find(edges[i][1])
                parent[a] = b
                i++
            }
            ans[idx] = find(p) == find(q)
        }
        return ans
    }
}
