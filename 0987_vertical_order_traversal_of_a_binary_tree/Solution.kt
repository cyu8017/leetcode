// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun verticalTraversal(root: TreeNode?): MutableList<MutableList<Int>> {
var nodes: MutableList<IntArray> = mutableListOf()
dfs(root, 0, 0, nodes)
nodes.sort(if ((a, b) -> a[0] != b[0]) a[0] - b[0] else (a[1] != b[1] ? a[1] - b[1] : a[2] - b[2]))
var byCol: java.util.TreeMap<Int, MutableList<Int>> = java.util.TreeMap()
for (t in nodes) {
byCol.getOrPut(t[0]) { mutableListOf() }.add(t[2])
}
return ArrayList(byCol.values())
}

    private fun dfs(node: TreeNode?, row: Int, col: Int, nodes: MutableList<IntArray>) {
if (node == null) {
return
}
nodes.add(intArrayOf( col, row, node.`val` ))
dfs(node.left, row + 1, col - 1, nodes)
dfs(node.right, row + 1, col + 1, nodes)
}
}
