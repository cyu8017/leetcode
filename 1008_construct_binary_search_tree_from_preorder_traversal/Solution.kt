// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var i = 0

    fun bstFromPreorder(preorder: IntArray): TreeNode? {
        i = 0
        return build(preorder, Int.MAX_VALUE)
    }

    private fun build(preorder: IntArray, bound: Int): TreeNode? {
        if (i == preorder.size || preorder[i] > bound) return null
        val root = TreeNode(preorder[i++])
        root.left = build(preorder, root.`val`)
        root.right = build(preorder, bound)
        return root
    }
}
