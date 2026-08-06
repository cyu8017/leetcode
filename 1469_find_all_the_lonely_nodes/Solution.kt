// LeetCode 1469 - Find All The Lonely Nodes
// https://leetcode.com/problems/find-all-the-lonely-nodes/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun getLonelyNodes(root: TreeNode?): List<Int> {
        val ans = mutableListOf<Int>()
        fun dfs(node: TreeNode?) {
            if (node == null) return
            val left = node.left
            val right = node.right
            if ((left == null) xor (right == null)) {
                ans.add((left ?: right)!!.`val`)
            }
            dfs(left)
            dfs(right)
        }
        dfs(root)
        return ans
    }
}
