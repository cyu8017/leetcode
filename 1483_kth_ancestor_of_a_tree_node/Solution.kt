// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

class TreeAncestor(n: Int, parent: IntArray) {
    private val up: Array<IntArray>

    init {
        val width = maxOf(1, 32 - Integer.numberOfLeadingZeros(n))
        up = Array(width) { IntArray(n) { -1 } }
        for (i in 0 until n) up[0][i] = parent[i]
        for (bit in 1 until width) {
            for (i in 0 until n) {
                val p = up[bit - 1][i]
                up[bit][i] = if (p == -1) -1 else up[bit - 1][p]
            }
        }
    }

    fun getKthAncestor(node: Int, k: Int): Int {
        var cur = node
        var steps = k
        var bit = 0
        while (steps > 0 && cur != -1) {
            if (steps and 1 == 1) {
                if (bit >= up.size) return -1
                cur = up[bit][cur]
            }
            bit++
            steps = steps shr 1
        }
        return cur
    }
}
