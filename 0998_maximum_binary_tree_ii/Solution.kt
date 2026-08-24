// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun insertIntoMaxTree(root: TreeNode?, `val`: Int): TreeNode? {
if (root == null || val > root.`val`) {
var node: TreeNode = TreeNode(val)
node.left = root
return node
}
root.right = insertIntoMaxTree(root.right, val)
return root
}
}
