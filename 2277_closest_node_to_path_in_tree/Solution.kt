// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

class Solution {

    val LOG: Int = 17

    var g: Array<MutableList<Int>>? = null

    var up: Array<IntArray>? = null

    var depth: IntArray? = null


    private fun dfs(u: Int, p: Int) {

            up[0][u] = p
            for (v in g[u]) {
                if (v != p) {
                    depth[v] = depth[u] + 1
                    dfs(v, u)
                }
            }

    }


    private fun lift(v: Int, d: Int): Int {
        var _v = v

            for (k in 0 until LOG) { if (((d >> k) & 1) != 0) _v = up[k][_v] }
            return _v
    }


    private fun lca(a: Int, b: Int): Int {
        var _a = a
        var _b = b

            if (depth[_a] < depth[_b]) {
                var t = _a
                _a = _b
                _b = t
            }
            _a = lift(_a, depth[_a] - depth[_b])
            if (_a == _b) return _a
            for (k in LOG - 1 downTo 0) {
                if (up[k][_a] != up[k][_b]) {
                    _a = up[k][_a]
                    _b = up[k][_b]
                }
            }
            return up[0][_a]
    }


    private fun dist(a: Int, b: Int): Int {

            var c = lca(a, b)
            return depth[a] + depth[b] - 2 * depth[c]

    }


    fun closestNode(n: Int, edges: Array<IntArray>, query: Array<IntArray>): IntArray {

            @SuppressWarnings("unchecked")
            var gg = arrayOfNulls<ArrayList>(n)
            g = gg
            for (i in 0 until n) { g[i] = ArrayList<Int>() }
            for (e in edges) {
                g[e[0]].add(e[1])
                g[e[1]].add(e[0])
            }
            up = Array(LOG) { IntArray(n) }
            depth = IntArray(n)
            dfs(0, 0)
            for (k in 1 until LOG) { for (var v = 0 } v < n; v++)
                    up[k][v] = up[k - 1][up[k - 1][v]]
            var ans = IntArray(query.size)
            for (i in 0 until query.size) {
                var a = query[i][0]; var b = query[i][1]; var x = query[i][2]
                var cands = intArrayOf(lca(a, b), lca(a, x), lca(b, x))
                var best = cands[0], bestD = dist(cands[0], x)
                for (t in 1 until 3) {
                    var d = dist(cands[t], x)
                    if (d < bestD) {
                        bestD = d
                        best = cands[t]
                    }
                }
                ans[i] = best
            }
            return ans

    }

}
