// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var postIndex = 0
    private lateinit var postorder: IntArray
    private lateinit var index: Map<Int, Int>

    fun buildTree(inorder: IntArray, postorder: IntArray): TreeNode? {
        this.postorder = postorder
        this.postIndex = postorder.size - 1
        this.index = inorder.withIndex().associate { it.value to it.index }
        return build(0, inorder.size - 1)
    }

    private fun build(left: Int, right: Int): TreeNode? {
        if (left > right) {
            return null
        }
        val rootVal = postorder[postIndex--]
        val mid = index[rootVal]!!
        val root = TreeNode(rootVal)
        root.right = build(mid + 1, right)
        root.left = build(left, mid - 1)
        return root
    }
}