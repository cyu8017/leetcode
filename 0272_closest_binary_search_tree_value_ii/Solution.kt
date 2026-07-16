// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun closestKValues(root: TreeNode?, target: Double, k: Int): List<Int> {
        val values = mutableListOf<Int>()
        inorder(root, values)

        var lo = 0
        var hi = values.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (values[mid] < target) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }

        var left = lo - 1
        var right = lo
        val result = mutableListOf<Int>()
        while (result.size < k) {
            if (right >= values.size ||
                (left >= 0 && kotlin.math.abs(values[left] - target) <= kotlin.math.abs(values[right] - target))
            ) {
                result.add(values[left])
                left--
            } else {
                result.add(values[right])
                right++
            }
        }
        return result
    }

    private fun inorder(node: TreeNode?, values: MutableList<Int>) {
        if (node == null) {
            return
        }
        inorder(node.left, values)
        values.add(node.`val`)
        inorder(node.right, values)
    }
}
