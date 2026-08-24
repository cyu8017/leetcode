// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private val depth: HashMap<Int, Int> = HashMap()
    private val parent: HashMap<Int, TreeNode> = HashMap()

    fun isCousins(root: TreeNode?, x: Int, y: Int): Boolean {
depth.clear()
parent.clear()
dfs(root, null, 0)
return depth[x].equals(depth[y]) && parent[x] != parent[y]
}

    private fun dfs(node: TreeNode?, p: TreeNode?, d: Int) {
if (node == null) {
return
}
depth.put(node.`val`, d)
parent.put(node.`val`, p)
dfs(node.left, node, d + 1)
dfs(node.right, node, d + 1)
}
}
