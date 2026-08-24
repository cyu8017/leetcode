// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun delNodes(root: TreeNode?, to_delete: IntArray): List<TreeNode?> {
        val delete = to_delete.toSet()
        val forest = mutableListOf<TreeNode?>()

        fun dfs(node: TreeNode?, isRoot: Boolean): TreeNode? {
            if (node == null) return null
            val removed = node.`val` in delete
            if (isRoot && !removed) forest.add(node)
            node.left = dfs(node.left, removed)
            node.right = dfs(node.right, removed)
            return if (removed) null else node
        }

        dfs(root, true)
        return forest
    }
}
