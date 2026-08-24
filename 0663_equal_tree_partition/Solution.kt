// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun checkEqualTree(root: TreeNode?): Boolean {
        val seen = HashSet<Int>()
        fun sum(node: TreeNode?, record: Boolean): Int {
            if (node == null) return 0
            val total = node.`val` + sum(node.left, true) + sum(node.right, true)
            if (record) seen.add(total)
            return total
        }
        val total = sum(root, false)
        return total % 2 == 0 && (total / 2) in seen
    }
}
