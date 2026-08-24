// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

class Solution {
    companion object {
        private const val MOD = 1000000007L
    }

    private fun multiply(a: Array<LongArray>, b: Array<LongArray>): Array<LongArray> {
        val c = Array(2) { LongArray(2) }
        for (i in 0 until 2) {
            for (j in 0 until 2) {
                for (k in 0 until 2) {
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
                }
            }
        }
        return c
    }

    fun gatePathXor(n: Int, parent: IntArray, gates: Array<IntArray>, queries: Array<IntArray>): Int {
        var logn = 1
        while ((1 shl logn) <= n) logn++
        val up = Array(logn) { IntArray(n) }
        val product = Array(logn) { Array(n) { Array(2) { LongArray(2) } } }
        val children = Array(n) { ArrayList<Int>() }
        for (node in 1 until n) children[parent[node]].add(node)
        val depth = IntArray(n)
        val order = ArrayList<Int>()
        order.add(0)
        var oi = 0
        while (oi < order.size) {
            val u = order[oi]
            for (v in children[u]) {
                depth[v] = depth[u] + 1
                order.add(v)
            }
            oi++
        }
        for (u in 0 until n) {
            up[0][u] = if (u == 0) 0 else parent[u]
            product[0][u] = arrayOf(
                longArrayOf(gates[u][1].toLong(), gates[u][2].toLong()),
                longArrayOf(gates[u][2].toLong(), gates[u][0].toLong())
            )
        }
        for (level in 1 until logn) {
            for (u in 0 until n) {
                val mid = up[level - 1][u]
                up[level][u] = up[level - 1][mid]
                product[level][u] = multiply(product[level - 1][u], product[level - 1][mid])
            }
        }
        var answer = 0
        for (query in queries) {
            val ancestor = lca(query[0], query[2], depth, up, logn)
            val alice = ways(query[0], query[1], depth[query[0]] - depth[ancestor], up, product)
            val bob = ways(query[2], query[3], depth[query[2]] - depth[ancestor], up, product)
            val total = (alice * bob % MOD).toInt()
            answer = answer xor total
        }
        return answer
    }

    private fun liftNode(node0: Int, distance0: Int, up: Array<IntArray>): Int {
        var node = node0
        var distance = distance0
        var level = 0
        while (distance > 0) {
            if ((distance and 1) != 0) node = up[level][node]
            distance = distance shr 1
            level++
        }
        return node
    }

    private fun lca(a0: Int, b0: Int, depth: IntArray, up: Array<IntArray>, logn: Int): Int {
        var a = a0
        var b = b0
        if (depth[a] > depth[b]) a = liftNode(a, depth[a] - depth[b], up)
        else if (depth[b] > depth[a]) b = liftNode(b, depth[b] - depth[a], up)
        if (a == b) return a
        for (level in logn - 1 downTo 0) {
            if (up[level][a] != up[level][b]) {
                a = up[level][a]
                b = up[level][b]
            }
        }
        return up[0][a]
    }

    private fun ways(node0: Int, card: Int, distance0: Int, up: Array<IntArray>, product: Array<Array<Array<LongArray>>>): Long {
        var node = node0
        var distance = distance0
        var vector = LongArray(2)
        vector[card] = 1
        var level = 0
        while (distance > 0) {
            if ((distance and 1) != 0) {
                val matrix = product[level][node]
                vector = longArrayOf(
                    (vector[0] * matrix[0][0] + vector[1] * matrix[1][0]) % MOD,
                    (vector[0] * matrix[0][1] + vector[1] * matrix[1][1]) % MOD
                )
                node = up[level][node]
            }
            distance = distance shr 1
            level++
        }
        return (vector[0] + vector[1]) % MOD
    }
}
