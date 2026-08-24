// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    private lateinit var postIndex: HashMap<Int, Int>
    private lateinit var preorder: IntArray

    fun constructFromPrePost(preorder: IntArray, postorder: IntArray): TreeNode? {
        this.preorder = preorder
        postIndex = HashMap()
        for (i in postorder.indices) postIndex[postorder[i]] = i
        val n = preorder.size
        return build(0, n - 1, 0, n - 1)
    }

    private fun build(preLo: Int, preHi: Int, postLo: Int, postHi: Int): TreeNode? {
        if (preLo > preHi) return null
        val root = TreeNode(preorder[preLo])
        if (preLo == preHi) return root
        val leftVal = preorder[preLo + 1]
        val leftPost = postIndex[leftVal]!!
        val leftSize = leftPost - postLo + 1
        root.left = build(preLo + 1, preLo + leftSize, postLo, leftPost)
        root.right = build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1)
        return root
    }
}
