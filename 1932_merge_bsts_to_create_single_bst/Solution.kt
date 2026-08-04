// LeetCode 1932
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun canMerge(trees: List<TreeNode>): TreeNode? {
        val valueToRoot = HashMap<Int, TreeNode>()
        val count = HashMap<Int, Int>()
        for (t in trees) {
            valueToRoot[t.`val`] = t
            count[t.`val`] = count.getOrDefault(t.`val`, 0) + 1
            t.left?.let { count[it.`val`] = count.getOrDefault(it.`val`, 0) + 1 }
            t.right?.let { count[it.`val`] = count.getOrDefault(it.`val`, 0) + 1 }
        }
        val roots = trees.filter { count[it.`val`] == 1 }
        if (roots.size != 1) return null
        val root = roots[0]
        fun merge(node: TreeNode?): Boolean {
            if (node == null) return true
            node.left?.let { left ->
                if (left.`val` in valueToRoot) node.left = valueToRoot.remove(left.`val`)
            }
            node.right?.let { right ->
                if (right.`val` in valueToRoot) node.right = valueToRoot.remove(right.`val`)
            }
            return merge(node.left) && merge(node.right)
        }
        valueToRoot.remove(root.`val`)
        if (!merge(root) || valueToRoot.isNotEmpty()) return null
        fun isValidBst(node: TreeNode?, lo: Long, hi: Long): Boolean {
            if (node == null) return true
            val v = node.`val`.toLong()
            if (v <= lo || v >= hi) return false
            return isValidBst(node.left, lo, v) && isValidBst(node.right, v, hi)
        }
        return if (isValidBst(root, Long.MIN_VALUE, Long.MAX_VALUE)) root else null
    }
}
