// LeetCode 1315 - Sum of Nodes with Even-Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun sumEvenGrandparent(root: TreeNode?): Int {
        fun dfs(node: TreeNode?, parent: TreeNode?, grandparent: TreeNode?): Int {
            if (node == null) return 0
            val add = if (grandparent != null && grandparent.`val` % 2 == 0) node.`val` else 0
            return add + dfs(node.left, node, parent) + dfs(node.right, node, parent)
        }
        return dfs(root, null, null)
    }
}
