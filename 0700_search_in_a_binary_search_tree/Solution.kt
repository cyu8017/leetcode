// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun searchBST(root: TreeNode?, `val`: Int): TreeNode? {
        var root = root
        while (root != null && root.`val` != `val`) {
            root = if (`val` < root.`val`) root.left else root.right
        }
        return root
    }
}
