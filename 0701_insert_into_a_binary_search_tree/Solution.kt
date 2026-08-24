// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun insertIntoBST(root: TreeNode?, `val`: Int): TreeNode? {
        if (root == null) return TreeNode(`val`)
        var node = root
        while (true) {
            if (`val` < node!!.`val`) {
                if (node.left == null) {
                    node.left = TreeNode(`val`)
                    break
                }
                node = node.left
            } else {
                if (node.right == null) {
                    node.right = TreeNode(`val`)
                    break
                }
                node = node.right
            }
        }
        return root
    }
}
