// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

class Solution {
    private var tree: IntArray? = null
    private var size: Int = 0
    private var n: Int = 0

    fun numOfUnplacedFruits(fruits: IntArray, baskets: IntArray): Int {
        n = baskets.size
        size = 1
        while (size < n) size  shl = 1
        tree = IntArray(size * 2)
        for (i in 0 until n) { tree[size + i] = baskets[i] }
        run {
            var i = size - 1
            while (i > 0) {
                tree[i] = maxOf(tree[i * 2], tree[i * 2 + 1])
                i = i - 1
            }
        }
        var unplaced = 0
        for (f in fruits) {
            var idx = find(1, 0, size - 1, f)
            if (idx == -1 || idx >= n) unplaced++
            else update(idx)
        }
        return unplaced
    }

    private fun find(node: Int, nl: Int, nr: Int, need: Int): Int {
        if (tree[node] < need) return -1
        if (nl == nr) return nl
        var mid = (nl + nr) / 2
        var left = find(node * 2, nl, mid, need)
        if (left != -1) return left
        return find(node * 2 + 1, mid + 1, nr, need)
    }

    private fun update(idx: Int) {
        var p = size + idx
        tree[p] = -1
        for (p >>= 1; p > 0; p >>= 1) tree[p] = maxOf(tree[p * 2], tree[p * 2 + 1])
    }
}
