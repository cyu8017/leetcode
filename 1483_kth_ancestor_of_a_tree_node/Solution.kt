// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

class TreeAncestor(n: Int, parent: IntArray) {
    private val up = mutableListOf(parent.copyOf())

    init {
        val width = maxOf(1, 32 - Integer.numberOfLeadingZeros(n))
        for (b in 1 until width) {
            val prev = up[b - 1]
            val cur = IntArray(n) { i -> if (prev[i] == -1) -1 else prev[prev[i]] }
            up.add(cur)
        }
    }

    fun getKthAncestor(node: Int, k: Int): Int {
        var cur = node
        var steps = k
        var bit = 0
        while (steps > 0 && cur != -1) {
            if (steps and 1 != 0) {
                if (bit >= up.size) return -1
                cur = up[bit][cur]
            }
            bit++
            steps = steps shr 1
        }
        return cur
    }
}
