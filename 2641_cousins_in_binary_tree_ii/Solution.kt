
// LeetCode 2641 - Cousins in Binary Tree II
// https://leetcode.com/problems/cousins-in-binary-tree-ii/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun replaceValueInTree(root: TreeNode?): TreeNode? {
        if (root == null) return null
        root.`val` = 0
        val q = ArrayDeque<TreeNode>()
        q.add(root)
        while (q.isNotEmpty()) {
            val sz = q.size
            var levelSum = 0
            val level = ArrayList<TreeNode>()
            repeat(sz) {
                val node = q.removeFirst()
                level.add(node)
                if (node.left != null) levelSum += node.left!!.`val`
                if (node.right != null) levelSum += node.right!!.`val`
            }
            for (node in level) {
                var cousin = levelSum
                if (node.left != null) cousin -= node.left!!.`val`
                if (node.right != null) cousin -= node.right!!.`val`
                if (node.left != null) {
                    node.left!!.`val` = cousin
                    q.add(node.left!!)
                }
                if (node.right != null) {
                    node.right!!.`val` = cousin
                    q.add(node.right!!)
                }
            }
        }
        return root
    }
}
