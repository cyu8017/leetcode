// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals {
    private class SegNode {
        var left: SegNode? = null
        var right: SegNode? = null
        var covered = false
    }

    private var root: SegNode? = null
    private var cnt = 0

    private fun addRange(L: Int, R: Int, l: Int, r: Int, holder: Array<SegNode?>): IntArray {
        var node = holder[0]
        if (node == null) {
            node = SegNode()
            holder[0] = node
        }
        if (node.covered) return intArrayOf(0)
        if (l <= L && R <= r) {
            node.covered = true
            node.left = null
            node.right = null
            return intArrayOf(R - L + 1)
        }
        val mid = (L + R) / 2
        var added = 0
        if (l <= mid) {
            val leftH = arrayOf(node.left)
            added += addRange(L, mid, l, r, leftH)[0]
            node.left = leftH[0]
        }
        if (r > mid) {
            val rightH = arrayOf(node.right)
            added += addRange(mid + 1, R, l, r, rightH)[0]
            node.right = rightH[0]
        }
        if (node.left != null && node.right != null && node.left!!.covered && node.right!!.covered) {
            node.covered = true
            node.left = null
            node.right = null
        }
        return intArrayOf(added)
    }

    constructor() {}

    fun add(left: Int, right: Int) {
        val holder = arrayOf(root)
        cnt += addRange(1, 1_000_000_000, left, right, holder)[0]
        root = holder[0]
    }

    fun count(): Int {
        return cnt
    }
}
