// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

class Solution {
    fun areConnected(n: Int, threshold: Int, queries: Array<IntArray>): List<Boolean> {
        val parent = IntArray(n + 1) { it }
        fun find(x: Int): Int {
            var cur = x
            while (cur != parent[cur]) {
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            }
            return cur
        }
        for (d in threshold + 1..n) {
            var x = 2 * d
            while (x <= n) {
                val a = find(d)
                val b = find(x)
                if (a != b) parent[b] = a
                x += d
            }
        }
        return queries.map { find(it[0]) == find(it[1]) }
    }
}
