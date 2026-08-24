// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findDuplicateSubtrees(root: TreeNode?): List<TreeNode?> {
        val count = HashMap<String, Int>()
        val result = ArrayList<TreeNode?>()
        fun dfs(node: TreeNode?): String {
            if (node == null) return "#"
            val serial = node.`val`.toString() + "," + dfs(node.left) + "," + dfs(node.right)
            val c = count.getOrDefault(serial, 0) + 1
            count[serial] = c
            if (c == 2) result.add(node)
            return serial
        }
        dfs(root)
        return result
    }
}
