// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var preIndex = 0
    private lateinit var preorder: IntArray
    private lateinit var index: Map<Int, Int>

    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        this.preorder = preorder
        this.preIndex = 0
        this.index = inorder.withIndex().associate { it.value to it.index }
        return build(0, inorder.size - 1)
    }

    private fun build(left: Int, right: Int): TreeNode? {
        if (left > right) {
            return null
        }
        val rootVal = preorder[preIndex++]
        val mid = index[rootVal]!!
        val root = TreeNode(rootVal)
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    }
}